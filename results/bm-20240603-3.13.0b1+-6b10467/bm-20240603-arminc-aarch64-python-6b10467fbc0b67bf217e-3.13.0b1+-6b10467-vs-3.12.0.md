# Results vs. 3.12.0

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: linux-aarch64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.01x faster
- HPT reliability: 64.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 305 ms: 1.01x faster                                                     |
| docutils       | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                   |
| html5lib       | 65.1 ms                                                               | 67.4 ms: 1.04x slower                                                    |
| tornado_http   | 136 ms                                                                | 127 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 491 ms: 1.27x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 604 ms: 1.23x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 648 ms: 1.20x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 481 ms: 1.20x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 787 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 770 ms: 1.15x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                                 | 1.18x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.07x faster                                                     |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.84 ms: 1.04x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 191 ms: 1.02x faster                                                     |
| pickle_pure_python   | 365 us                                                                | 363 us: 1.01x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                   |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| pickle_dict          | 37.3 us                                                               | 38.0 us: 1.02x slower                                                    |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.35 us: 1.02x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 82.1 ms: 1.04x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.45 us: 1.05x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                    |
| python_startup         | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                    |
| django_template | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                                    |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 491 ms: 1.27x faster                                                     |
| comprehensions             | 25.4 us                                                               | 20.2 us: 1.26x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 604 ms: 1.23x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 648 ms: 1.20x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 481 ms: 1.20x faster                                                     |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.4 ms: 1.16x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 787 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 770 ms: 1.15x faster                                                     |
| mypy2                      | 873 ms                                                                | 770 ms: 1.13x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.28 sec: 1.10x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.06 us: 1.08x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.75 us: 1.08x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                     |
| regex_compile              | 137 ms                                                                | 129 ms: 1.07x faster                                                     |
| dulwich_log                | 62.0 ms                                                               | 58.2 ms: 1.06x faster                                                    |
| tornado_http               | 136 ms                                                                | 127 ms: 1.06x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.88 ms: 1.06x faster                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 82.0 ms: 1.06x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.05x faster                                                    |
| chaos                      | 71.4 ms                                                               | 68.2 ms: 1.05x faster                                                    |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 23.5 ms: 1.05x faster                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.26 ms: 1.04x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.41 ms: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 21.0 ms: 1.03x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 142 ms: 1.03x faster                                                     |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.02x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 191 ms: 1.02x faster                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 84.2 ms: 1.01x faster                                                    |
| 2to3                       | 308 ms                                                                | 305 ms: 1.01x faster                                                     |
| pickle_pure_python         | 365 us                                                                | 363 us: 1.01x faster                                                     |
| tomli_loads                | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                                     |
| deepcopy                   | 446 us                                                                | 452 us: 1.01x slower                                                     |
| fannkuch                   | 443 ms                                                                | 450 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.02x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 62.4 ms: 1.02x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 38.0 us: 1.02x slower                                                    |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                                     |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                    |
| json                       | 5.54 ms                                                               | 5.65 ms: 1.02x slower                                                    |
| pickle_list                | 5.25 us                                                               | 5.35 us: 1.02x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.5 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 935 ms: 1.02x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                    |
| sympy_expand               | 454 ms                                                                | 463 ms: 1.02x slower                                                     |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 129 ms: 1.02x slower                                                     |
| thrift                     | 937 us                                                                | 964 us: 1.03x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.20 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.64 ms: 1.03x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.08 sec: 1.03x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 67.4 ms: 1.04x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.91 us: 1.04x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 82.1 ms: 1.04x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 590 ms: 1.04x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.84 ms: 1.04x slower                                                    |
| gunicorn                   | 1.14 ms                                                               | 1.18 ms: 1.04x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.45 us: 1.05x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 52.0 us: 1.05x slower                                                    |
| logging_silent             | 127 ns                                                                | 134 ns: 1.05x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.53 ms: 1.05x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.3 ms: 1.06x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                    |
| scimark_fft                | 418 ms                                                                | 448 ms: 1.07x slower                                                     |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                     |
| scimark_sor                | 150 ms                                                                | 161 ms: 1.08x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 30.6 ms: 1.08x slower                                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 197 us: 1.09x slower                                                     |
| richards                   | 50.9 ms                                                               | 56.5 ms: 1.11x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.9 ms: 1.13x slower                                                    |
| python_startup             | 11.4 ms                                                               | 13.0 ms: 1.14x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.07 ms: 1.15x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.37 ms: 1.24x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (15): pylint, xml_etree_iterparse, dask, pycparser, async_generators, genshi_xml, float, pyflate, nqueens, asyncio_websockets, deepcopy_reduce, bench_mp_pool, coroutines, chameleon, aiohttp
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240603-3.13.0b1+-6b10467/bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467.json: flaskblogging

# HPT report

- Reliability score: 64.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x