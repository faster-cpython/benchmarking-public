# Results vs. 3.12.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.025x faster
- HPT reliability: 93.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                     |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                   |
| tornado_http   | 136 ms                                                                | 125 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 528 ms: 1.40x faster                                                     |
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 578 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 438 ms: 1.32x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 743 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 733 ms: 1.21x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| float          | 92.1 ms                                                               | 95.1 ms: 1.03x slower                                                    |
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 31.9 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.03x faster                                                     |
| unpickle_pure_python | 260 us                                                                | 257 us: 1.01x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 371 us: 1.02x slower                                                     |
| json_loads           | 30.7 us                                                               | 31.3 us: 1.02x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.67 ms: 1.04x slower                                                    |
| python_startup         | 11.4 ms                                                               | 15.6 ms: 1.37x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.19x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 60.1 ms: 1.01x faster                                                    |
| django_template | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                    |
| mako            | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 528 ms: 1.40x faster                                                     |
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 578 ms: 1.34x faster                                                     |
| deepcopy                   | 446 us                                                                | 336 us: 1.32x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 438 ms: 1.32x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 38.4 us: 1.29x faster                                                    |
| generators                 | 43.5 ms                                                               | 34.8 ms: 1.25x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.13 sec: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 743 ms: 1.23x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.8 us: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 733 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.54 us: 1.16x faster                                                    |
| go                         | 157 ms                                                                | 137 ms: 1.15x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.5 ms: 1.14x faster                                                    |
| raytrace                   | 353 ms                                                                | 310 ms: 1.14x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 140 ms: 1.12x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.91 us: 1.11x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.62 us: 1.10x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 142 ms: 1.08x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.4 ms: 1.08x faster                                                    |
| tornado_http               | 136 ms                                                                | 125 ms: 1.08x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 135 ms: 1.08x faster                                                     |
| sympy_str                  | 280 ms                                                                | 264 ms: 1.06x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 58.7 ms: 1.06x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.74 ms: 1.05x faster                                                    |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 82.7 ms: 1.05x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.94 ms: 1.04x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                    |
| async_generators           | 491 ms                                                                | 477 ms: 1.03x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.03x faster                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.28 ms: 1.02x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 21.2 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.3 ms: 1.02x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                   |
| pycparser                  | 1.26 sec                                                              | 1.24 sec: 1.02x faster                                                   |
| json                       | 5.54 ms                                                               | 5.46 ms: 1.01x faster                                                    |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.01x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 257 us: 1.01x faster                                                     |
| genshi_xml                 | 60.6 ms                                                               | 60.1 ms: 1.01x faster                                                    |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.0 ms: 1.01x slower                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| sympy_expand               | 454 ms                                                                | 459 ms: 1.01x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 128 ms: 1.02x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 371 us: 1.02x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                                    |
| json_loads                 | 30.7 us                                                               | 31.3 us: 1.02x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 939 ms: 1.03x slower                                                     |
| richards_super             | 58.5 ms                                                               | 60.0 ms: 1.03x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                    |
| float                      | 92.1 ms                                                               | 95.1 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.67 ms: 1.04x slower                                                    |
| logging_silent             | 127 ns                                                                | 132 ns: 1.04x slower                                                     |
| pyflate                    | 559 ms                                                                | 585 ms: 1.05x slower                                                     |
| scimark_fft                | 418 ms                                                                | 438 ms: 1.05x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.6 ms: 1.05x slower                                                    |
| fannkuch                   | 443 ms                                                                | 468 ms: 1.06x slower                                                     |
| richards                   | 50.9 ms                                                               | 53.9 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.57 ms: 1.06x slower                                                    |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 194 us: 1.07x slower                                                     |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.10x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.45 ms: 1.11x slower                                                    |
| coverage                   | 87.3 ms                                                               | 97.2 ms: 1.11x slower                                                    |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 31.9 ms: 1.13x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.1 ms: 1.15x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.6 ms: 1.37x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.31 ms: 1.43x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.60 ms: 1.88x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 4.94 sec: 700.57x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (9): chaos, pylint, regex_dna, nqueens, asyncio_websockets, html5lib, genshi_text, thrift, xml_etree_generate
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 93.77% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x