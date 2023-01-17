
# Results vs. base

- fork: faster-cpython
- ref: fstring_with_intrins
- machine: linux-x86_64
- commit hash: df06ef8
- commit date: 2023-01-13
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 253 ms: 1.01x slower                                                             |
| chameleon      | 6.25 ms                                                                | 6.37 ms: 1.02x slower                                                            |
| docutils       | 2.48 sec                                                               | 2.51 sec: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 71.7 ms                                                                | 72.2 ms: 1.01x slower                                                            |
| nbody          | 97.0 ms                                                                | 93.7 ms: 1.04x faster                                                            |
| pidigits       | 197 ms                                                                 | 189 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 130 ms: 1.01x slower                                                             |
| regex_dna      | 203 ms                                                                 | 210 ms: 1.03x slower                                                             |
| regex_effbot   | 3.43 ms                                                                | 3.58 ms: 1.04x slower                                                            |
| regex_v8       | 21.6 ms                                                                | 21.8 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps          | 9.35 ms                                                                | 9.46 ms: 1.01x slower                                                            |
| json_loads          | 24.4 us                                                                | 24.0 us: 1.02x faster                                                            |
| pickle              | 9.86 us                                                                | 10.1 us: 1.03x slower                                                            |
| pickle_dict         | 30.0 us                                                                | 30.7 us: 1.02x slower                                                            |
| pickle_list         | 3.99 us                                                                | 4.10 us: 1.03x slower                                                            |
| unpickle_list       | 4.88 us                                                                | 4.97 us: 1.02x slower                                                            |
| xml_etree_iterparse | 107 ms                                                                 | 105 ms: 1.02x faster                                                             |
| xml_etree_generate  | 76.3 ms                                                                | 77.5 ms: 1.01x slower                                                            |
| xml_etree_process   | 53.4 ms                                                                | 53.8 ms: 1.01x slower                                                            |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.54 ms                                                                | 8.57 ms: 1.00x slower                                                            |
| python_startup_no_site | 6.11 ms                                                                | 6.13 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 32.2 ms: 1.01x slower                                                            |
| genshi_text     | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                                            |
| mako            | 9.71 ms                                                                | 9.75 ms: 1.00x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3                    | 251 ms                                                                 | 253 ms: 1.01x slower                                                             |
| aiohttp                 | 997 us                                                                 | 1.00 ms: 1.00x slower                                                            |
| async_generators        | 351 ms                                                                 | 355 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed | 737 ms                                                                 | 745 ms: 1.01x slower                                                             |
| async_tree_io           | 1.32 sec                                                               | 1.33 sec: 1.01x slower                                                           |
| async_tree_memoization  | 617 ms                                                                 | 656 ms: 1.06x slower                                                             |
| asyncio_tcp             | 505 ms                                                                 | 504 ms: 1.00x faster                                                             |
| chameleon               | 6.25 ms                                                                | 6.37 ms: 1.02x slower                                                            |
| chaos                   | 68.0 ms                                                                | 66.9 ms: 1.02x faster                                                            |
| coverage                | 97.7 ms                                                                | 99.6 ms: 1.02x slower                                                            |
| crypto_pyaes            | 74.8 ms                                                                | 74.3 ms: 1.01x faster                                                            |
| deepcopy                | 329 us                                                                 | 332 us: 1.01x slower                                                             |
| deepcopy_memo           | 33.7 us                                                                | 33.5 us: 1.01x faster                                                            |
| deltablue               | 3.17 ms                                                                | 3.19 ms: 1.01x slower                                                            |
| django_template         | 31.9 ms                                                                | 32.2 ms: 1.01x slower                                                            |
| djangocms               | 32.2 us                                                                | 32.8 us: 1.02x slower                                                            |
| docutils                | 2.48 sec                                                               | 2.51 sec: 1.01x slower                                                           |
| dulwich_log             | 62.2 ms                                                                | 61.6 ms: 1.01x faster                                                            |
| float                   | 71.7 ms                                                                | 72.2 ms: 1.01x slower                                                            |
| create_gc_cycles        | 1.44 ms                                                                | 1.46 ms: 1.01x slower                                                            |
| gc_traversal            | 4.05 ms                                                                | 3.79 ms: 1.07x faster                                                            |
| generators              | 75.7 ms                                                                | 77.2 ms: 1.02x slower                                                            |
| genshi_text             | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                                            |
| go                      | 134 ms                                                                 | 134 ms: 1.01x faster                                                             |
| gunicorn                | 1.07 ms                                                                | 1.07 ms: 1.01x slower                                                            |
| hexiom                  | 6.03 ms                                                                | 5.95 ms: 1.01x faster                                                            |
| json_dumps              | 9.35 ms                                                                | 9.46 ms: 1.01x slower                                                            |
| json_loads              | 24.4 us                                                                | 24.0 us: 1.02x faster                                                            |
| logging_format          | 6.22 us                                                                | 6.31 us: 1.02x slower                                                            |
| logging_silent          | 89.4 ns                                                                | 91.5 ns: 1.02x slower                                                            |
| logging_simple          | 5.66 us                                                                | 5.71 us: 1.01x slower                                                            |
| mako                    | 9.71 ms                                                                | 9.75 ms: 1.00x slower                                                            |
| mdp                     | 2.69 sec                                                               | 2.47 sec: 1.09x faster                                                           |
| nbody                   | 97.0 ms                                                                | 93.7 ms: 1.04x faster                                                            |
| nqueens                 | 77.8 ms                                                                | 79.4 ms: 1.02x slower                                                            |
| pathlib                 | 17.7 ms                                                                | 17.9 ms: 1.01x slower                                                            |
| pickle                  | 9.86 us                                                                | 10.1 us: 1.03x slower                                                            |
| pickle_dict             | 30.0 us                                                                | 30.7 us: 1.02x slower                                                            |
| pickle_list             | 3.99 us                                                                | 4.10 us: 1.03x slower                                                            |
| pidigits                | 197 ms                                                                 | 189 ms: 1.04x faster                                                             |
| pprint_safe_repr        | 663 ms                                                                 | 666 ms: 1.00x slower                                                             |
| pprint_pformat          | 1.38 sec                                                               | 1.37 sec: 1.01x faster                                                           |
| pycparser               | 1.09 sec                                                               | 1.09 sec: 1.01x faster                                                           |
| pyflate                 | 401 ms                                                                 | 394 ms: 1.02x faster                                                             |
| python_startup          | 8.54 ms                                                                | 8.57 ms: 1.00x slower                                                            |
| python_startup_no_site  | 6.11 ms                                                                | 6.13 ms: 1.00x slower                                                            |
| raytrace                | 279 ms                                                                 | 287 ms: 1.03x slower                                                             |
| regex_compile           | 129 ms                                                                 | 130 ms: 1.01x slower                                                             |
| regex_dna               | 203 ms                                                                 | 210 ms: 1.03x slower                                                             |
| regex_effbot            | 3.43 ms                                                                | 3.58 ms: 1.04x slower                                                            |
| regex_v8                | 21.6 ms                                                                | 21.8 ms: 1.01x slower                                                            |
| richards                | 41.2 ms                                                                | 42.3 ms: 1.03x slower                                                            |
| scimark_sparse_mat_mult | 4.15 ms                                                                | 4.01 ms: 1.04x faster                                                            |
| spectral_norm           | 94.5 ms                                                                | 97.6 ms: 1.03x slower                                                            |
| sqlglot_transpile       | 1.68 ms                                                                | 1.69 ms: 1.01x slower                                                            |
| sqlglot_optimize        | 50.6 ms                                                                | 51.0 ms: 1.01x slower                                                            |
| sqlglot_normalize       | 105 ms                                                                 | 105 ms: 1.00x slower                                                             |
| sqlite_synth            | 2.61 us                                                                | 2.56 us: 1.02x faster                                                            |
| sympy_expand            | 454 ms                                                                 | 457 ms: 1.01x slower                                                             |
| unpack_sequence         | 44.5 ns                                                                | 43.0 ns: 1.04x faster                                                            |
| unpickle_list           | 4.88 us                                                                | 4.97 us: 1.02x slower                                                            |
| xml_etree_iterparse     | 107 ms                                                                 | 105 ms: 1.02x faster                                                             |
| xml_etree_generate      | 76.3 ms                                                                | 77.5 ms: 1.01x slower                                                            |
| xml_etree_process       | 53.4 ms                                                                | 53.8 ms: 1.01x slower                                                            |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (27): async_tree_none, bench_mp_pool, bench_thread_pool, coroutines, dask, deepcopy_reduce, fannkuch, genshi_xml, html5lib, json, meteor_contest, mypy, pickle_pure_python, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, sqlglot_parse, sympy_integrate, sympy_sum, sympy_str, telco, thrift, tornado_http, unpickle, unpickle_pure_python, xml_etree_parse
