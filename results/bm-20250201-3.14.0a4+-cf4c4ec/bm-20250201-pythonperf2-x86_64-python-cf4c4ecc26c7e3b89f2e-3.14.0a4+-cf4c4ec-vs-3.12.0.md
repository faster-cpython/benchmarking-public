# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 278 ms: 1.03x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 640 ms: 1.65x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 639 ms: 1.63x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                         |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.60x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 344 ms: 1.58x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 503 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 514 ms: 1.36x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.55x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.10 ms: 1.15x faster                                                        |
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                         |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|---------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse | 103 ms                                                       | 96.1 ms: 1.07x faster                                                        |
| tomli_loads         | 2.16 sec                                                     | 2.03 sec: 1.06x faster                                                       |
| xml_etree_parse     | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| unpickle            | 14.8 us                                                      | 14.1 us: 1.05x faster                                                        |
| xml_etree_generate  | 86.1 ms                                                      | 83.4 ms: 1.03x faster                                                        |
| pickle_pure_python  | 318 us                                                       | 325 us: 1.02x slower                                                         |
| unpickle_list       | 4.66 us                                                      | 4.92 us: 1.06x slower                                                        |
| pickle_dict         | 32.5 us                                                      | 34.9 us: 1.07x slower                                                        |
| json_loads          | 24.4 us                                                      | 26.5 us: 1.09x slower                                                        |
| json_dumps          | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| pickle              | 10.5 us                                                      | 12.4 us: 1.18x slower                                                        |
| pickle_list         | 4.43 us                                                      | 5.42 us: 1.22x slower                                                        |
| Geometric mean      | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                        |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 640 ms: 1.65x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 639 ms: 1.63x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                         |
| async_tree_none            | 452 ms                                                       | 283 ms: 1.60x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 344 ms: 1.58x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 503 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 514 ms: 1.36x faster                                                         |
| deepcopy                   | 368 us                                                       | 280 us: 1.31x faster                                                         |
| comprehensions             | 21.9 us                                                      | 16.9 us: 1.30x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.4 ms: 1.27x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.6 us: 1.24x faster                                                        |
| go                         | 150 ms                                                       | 122 ms: 1.23x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 15.6 ms: 1.21x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 45.7 ns: 1.16x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.10 ms: 1.15x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.59 us: 1.14x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 141 ms: 1.13x faster                                                         |
| raytrace                   | 298 ms                                                       | 264 ms: 1.13x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.7 ms: 1.12x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.02 us: 1.12x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.2 ms: 1.11x faster                                                        |
| float                      | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 83.2 ms: 1.10x faster                                                        |
| django_template            | 38.2 ms                                                      | 34.9 ms: 1.09x faster                                                        |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                         |
| chaos                      | 64.0 ms                                                      | 59.3 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 96.1 ms: 1.07x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.6 ms: 1.06x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.03 sec: 1.06x faster                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.30 ms: 1.06x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 93.4 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.68 ms: 1.06x faster                                                        |
| sympy_str                  | 302 ms                                                       | 287 ms: 1.05x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.05x faster                                                       |
| unpickle                   | 14.8 us                                                      | 14.1 us: 1.05x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 771 ms: 1.05x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| meteor_contest             | 128 ms                                                       | 123 ms: 1.04x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 83.4 ms: 1.03x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 925 us: 1.03x faster                                                         |
| 2to3                       | 285 ms                                                       | 278 ms: 1.03x faster                                                         |
| pycparser                  | 1.23 sec                                                     | 1.20 sec: 1.03x faster                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 56.1 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 116 ms                                                       | 114 ms: 1.02x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 373 ms: 1.01x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.83 sec: 1.01x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 89.0 ms: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                         |
| scimark_fft                | 301 ms                                                       | 300 ms: 1.00x faster                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                       |
| scimark_sor                | 109 ms                                                       | 109 ms: 1.00x faster                                                         |
| sympy_expand               | 484 ms                                                       | 486 ms: 1.00x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 65.8 ms: 1.01x slower                                                        |
| pyflate                    | 439 ms                                                       | 443 ms: 1.01x slower                                                         |
| richards_super             | 51.3 ms                                                      | 51.9 ms: 1.01x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.04 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 325 us: 1.02x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 96.5 ns: 1.02x slower                                                        |
| async_generators           | 390 ms                                                       | 401 ms: 1.03x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.92 us: 1.06x slower                                                        |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 34.9 us: 1.07x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.55 ms: 1.08x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.5 us: 1.09x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 169 us: 1.12x slower                                                         |
| telco                      | 6.96 ms                                                      | 7.88 ms: 1.13x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| coverage                   | 66.7 ms                                                      | 76.8 ms: 1.15x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.4 us: 1.18x slower                                                        |
| pickle_list                | 4.43 us                                                      | 5.42 us: 1.22x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.77 ms: 1.74x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.23 ms: 1.79x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.76 sec: 369.23x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (7): richards, fannkuch, xml_etree_process, nbody, unpickle_pure_python, deltablue, asyncio_websockets
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x