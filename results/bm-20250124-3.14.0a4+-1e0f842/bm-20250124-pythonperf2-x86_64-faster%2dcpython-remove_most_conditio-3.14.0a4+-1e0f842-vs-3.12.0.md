# Results vs. 3.12.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.055x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 280 ms: 1.02x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 645 ms: 1.63x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 645 ms: 1.61x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.56x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 68.7 ms: 1.12x faster                                                                  |
| pidigits       | 265 ms                                                       | 254 ms: 1.05x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                                  |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                                   |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                                   |
| regex_v8       | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                                 |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                                   |
| unpickle_pure_python | 210 us                                                       | 205 us: 1.02x faster                                                                   |
| xml_etree_generate   | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 58.7 ms: 1.00x slower                                                                  |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.02x slower                                                                   |
| pickle_pure_python   | 318 us                                                       | 323 us: 1.02x slower                                                                   |
| json_loads           | 24.4 us                                                      | 25.6 us: 1.05x slower                                                                  |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                                  |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.37x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.8 ms: 1.07x faster                                                                  |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 645 ms: 1.63x faster                                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 645 ms: 1.61x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 350 ms: 1.56x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                                   |
| generators                 | 37.4 ms                                                      | 28.0 ms: 1.34x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                                   |
| deepcopy                   | 368 us                                                       | 282 us: 1.31x faster                                                                   |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 30.2 us: 1.22x faster                                                                  |
| go                         | 150 ms                                                       | 125 ms: 1.20x faster                                                                   |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                                  |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                                  |
| raytrace                   | 298 ms                                                       | 263 ms: 1.13x faster                                                                   |
| float                      | 76.6 ms                                                      | 68.7 ms: 1.12x faster                                                                  |
| sqlalchemy_declarative     | 159 ms                                                       | 143 ms: 1.11x faster                                                                   |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.0 ms: 1.11x faster                                                                  |
| coroutines                 | 23.0 ms                                                      | 20.7 ms: 1.11x faster                                                                  |
| logging_format             | 7.48 us                                                      | 6.75 us: 1.11x faster                                                                  |
| spectral_norm              | 91.6 ms                                                      | 83.2 ms: 1.10x faster                                                                  |
| chaos                      | 64.0 ms                                                      | 58.2 ms: 1.10x faster                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 73.8 ms: 1.09x faster                                                                  |
| logging_simple             | 6.71 us                                                      | 6.17 us: 1.09x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                                   |
| django_template            | 38.2 ms                                                      | 35.8 ms: 1.07x faster                                                                  |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                                   |
| scimark_lu                 | 98.8 ms                                                      | 93.1 ms: 1.06x faster                                                                  |
| tomli_loads                | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                                  |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                                   |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.05x faster                                                                 |
| mdp                        | 2.57 sec                                                     | 2.44 sec: 1.05x faster                                                                 |
| sympy_str                  | 302 ms                                                       | 288 ms: 1.05x faster                                                                   |
| sqlglot_parse              | 1.38 ms                                                      | 1.31 ms: 1.05x faster                                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.70 ms: 1.05x faster                                                                  |
| pidigits                   | 265 ms                                                       | 254 ms: 1.05x faster                                                                   |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                                  |
| pprint_safe_repr           | 807 ms                                                       | 778 ms: 1.04x faster                                                                   |
| bench_thread_pool          | 950 us                                                       | 922 us: 1.03x faster                                                                   |
| sqlglot_normalize          | 116 ms                                                       | 113 ms: 1.03x faster                                                                   |
| unpickle_pure_python       | 210 us                                                       | 205 us: 1.02x faster                                                                   |
| xml_etree_generate         | 86.1 ms                                                      | 84.1 ms: 1.02x faster                                                                  |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                                 |
| scimark_sor                | 109 ms                                                       | 107 ms: 1.02x faster                                                                   |
| 2to3                       | 285 ms                                                       | 280 ms: 1.02x faster                                                                   |
| nqueens                    | 89.9 ms                                                      | 88.7 ms: 1.01x faster                                                                  |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                                   |
| sqlglot_optimize           | 57.5 ms                                                      | 57.1 ms: 1.01x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                                   |
| xml_etree_process          | 58.4 ms                                                      | 58.7 ms: 1.00x slower                                                                  |
| hexiom                     | 5.96 ms                                                      | 6.02 ms: 1.01x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 3.28 ms: 1.01x slower                                                                  |
| dulwich_log                | 65.4 ms                                                      | 66.3 ms: 1.01x slower                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.02x slower                                                                   |
| pickle_pure_python         | 318 us                                                       | 323 us: 1.02x slower                                                                   |
| sympy_expand               | 484 ms                                                       | 493 ms: 1.02x slower                                                                   |
| pyflate                    | 439 ms                                                       | 452 ms: 1.03x slower                                                                   |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                                                   |
| logging_silent             | 94.4 ns                                                      | 97.4 ns: 1.03x slower                                                                  |
| async_generators           | 390 ms                                                       | 405 ms: 1.04x slower                                                                   |
| python_startup_no_site     | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                                  |
| json                       | 5.12 ms                                                      | 5.36 ms: 1.05x slower                                                                  |
| json_loads                 | 24.4 us                                                      | 25.6 us: 1.05x slower                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.51 ms: 1.07x slower                                                                  |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                                  |
| regex_v8                   | 23.6 ms                                                      | 26.3 ms: 1.11x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.14x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 76.5 ms: 1.15x slower                                                                  |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                                   |
| telco                      | 6.96 ms                                                      | 8.03 ms: 1.15x slower                                                                  |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.37x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 2.78 ms: 1.75x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 6.32 ms: 1.82x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 1.02 sec: 213.32x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                           |

Benchmark hidden because not significant (7): richards, asyncio_websockets, scimark_fft, nbody, docutils, sqlite_synth, richards_super
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250124-3.14.0a4+-1e0f842/bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x