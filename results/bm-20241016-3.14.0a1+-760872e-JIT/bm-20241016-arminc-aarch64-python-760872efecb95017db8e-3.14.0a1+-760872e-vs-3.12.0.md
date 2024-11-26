# Results vs. 3.12.0

- fork: python
- ref: 760872efecb95017db8e
- machine: linux-aarch64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.081x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 381 ms: 1.24x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.65 sec: 1.22x slower                                                   |
| html5lib       | 65.1 ms                                                               | 71.5 ms: 1.10x slower                                                    |
| tornado_http   | 136 ms                                                                | 147 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 540 ms: 1.37x faster                                                     |
| async_tree_none            | 624 ms                                                                | 455 ms: 1.37x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 597 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 446 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 752 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 734 ms: 1.21x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.20x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| float          | 92.1 ms                                                               | 98.0 ms: 1.06x slower                                                    |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 244 ms: 1.04x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 31.4 ms: 1.11x slower                                                    |
| regex_compile  | 137 ms                                                                | 169 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 188 ms: 1.04x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.5 ms: 1.02x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                   |
| json_loads           | 30.7 us                                                               | 31.4 us: 1.02x slower                                                    |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.0 us: 1.03x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 268 us: 1.03x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 389 us: 1.06x slower                                                     |
| unpickle_list        | 6.17 us                                                               | 6.67 us: 1.08x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                    |
| python_startup         | 11.4 ms                                                               | 14.6 ms: 1.29x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 33.5 ms: 1.22x slower                                                    |
| django_template | 40.7 ms                                                               | 51.1 ms: 1.26x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 81.5 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 540 ms: 1.37x faster                                                     |
| async_tree_none            | 624 ms                                                                | 455 ms: 1.37x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 597 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 446 ms: 1.29x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 38.9 us: 1.28x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 752 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 734 ms: 1.21x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.18 sec: 1.20x faster                                                   |
| deepcopy                   | 446 us                                                                | 377 us: 1.18x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.14x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                   |
| regex_dna                  | 254 ms                                                                | 244 ms: 1.04x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 188 ms: 1.04x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.96 us: 1.04x faster                                                    |
| comprehensions             | 25.4 us                                                               | 24.7 us: 1.03x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.47 us: 1.02x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.18 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.5 ms: 1.02x faster                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                    |
| raytrace                   | 353 ms                                                                | 358 ms: 1.01x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.02x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 80.5 ms: 1.02x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                   |
| thrift                     | 937 us                                                                | 957 us: 1.02x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                                   |
| json_loads                 | 30.7 us                                                               | 31.4 us: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.0 us: 1.03x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 268 us: 1.03x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.04x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.92 us: 1.04x slower                                                    |
| async_generators           | 491 ms                                                                | 510 ms: 1.04x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.27 sec: 1.04x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 90.2 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                    |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.85 ms: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 157 ms: 1.05x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.1 ms: 1.06x slower                                                    |
| float                      | 92.1 ms                                                               | 98.0 ms: 1.06x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 389 us: 1.06x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.67 us: 1.08x slower                                                    |
| tornado_http               | 136 ms                                                                | 147 ms: 1.09x slower                                                     |
| scimark_fft                | 418 ms                                                                | 456 ms: 1.09x slower                                                     |
| pyflate                    | 559 ms                                                                | 612 ms: 1.10x slower                                                     |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.52 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.5 ms: 1.10x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.4 ms: 1.11x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 629 ms: 1.11x slower                                                     |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.11x slower                                                     |
| fannkuch                   | 443 ms                                                                | 495 ms: 1.12x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.61 ms: 1.13x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.9 ms: 1.13x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.19 ms: 1.16x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.70 ms: 1.16x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.3 ms: 1.17x slower                                                    |
| go                         | 157 ms                                                                | 184 ms: 1.17x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.48 sec: 1.18x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 214 us: 1.19x slower                                                     |
| spectral_norm              | 131 ms                                                                | 155 ms: 1.19x slower                                                     |
| chaos                      | 71.4 ms                                                               | 85.0 ms: 1.19x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.18 ms: 1.19x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 33.5 ms: 1.22x slower                                                    |
| richards_super             | 58.5 ms                                                               | 71.5 ms: 1.22x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.65 sec: 1.22x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 122 ms: 1.23x slower                                                     |
| regex_compile              | 137 ms                                                                | 169 ms: 1.23x slower                                                     |
| 2to3                       | 308 ms                                                                | 381 ms: 1.24x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 156 ms: 1.24x slower                                                     |
| django_template            | 40.7 ms                                                               | 51.1 ms: 1.26x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 78.0 ms: 1.26x slower                                                    |
| richards                   | 50.9 ms                                                               | 64.3 ms: 1.26x slower                                                    |
| sympy_str                  | 280 ms                                                                | 358 ms: 1.28x slower                                                     |
| python_startup             | 11.4 ms                                                               | 14.6 ms: 1.29x slower                                                    |
| sympy_expand               | 454 ms                                                                | 592 ms: 1.31x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 1.20 sec: 1.31x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 81.8 ms: 1.33x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 81.5 ms: 1.35x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 29.1 ms: 1.35x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.54 sec: 1.35x slower                                                   |
| generators                 | 43.5 ms                                                               | 59.0 ms: 1.36x slower                                                    |
| pylint                     | 355 ms                                                                | 492 ms: 1.39x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 215 ms: 1.39x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 6.43 ms: 1.46x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.2 ms: 1.47x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.71 ms: 1.94x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.59 sec: 225.24x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.15x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_iterparse, pickle_list, asyncio_websockets, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.081x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.11x