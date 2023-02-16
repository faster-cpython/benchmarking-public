
# Results vs. 3.11.0

- fork: faster-cpython
- ref: fstring_with_intrins
- machine: linux-x86_64
- commit hash: df06ef8
- commit date: 2023-01-13
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                             |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                           |
| html5lib       | 64.8 ms                                                | 60.2 ms: 1.08x faster                                                            |
| tornado_http   | 96.5 ms                                                | 93.4 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                            |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                             |
| nbody          | 90.0 ms                                                | 93.7 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                             |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                            |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                             |
| regex_effbot   | 3.46 ms                                                | 3.58 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.46 ms: 1.31x faster                                                            |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                             |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                                             |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                                            |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.07x faster                                                             |
| pickle_dict          | 31.2 us                                                | 30.7 us: 1.02x faster                                                            |
| pickle_list          | 4.14 us                                                | 4.10 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                             |
| xml_etree_generate   | 75.9 ms                                                | 77.5 ms: 1.02x slower                                                            |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (3): unpickle, unpickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.57 ms: 1.00x faster                                                            |
| python_startup_no_site | 6.04 ms                                                | 6.13 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                            |
| genshi_text    | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                            |
| mako           | 9.83 ms                                                | 9.75 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 504 ms: 1.75x faster                                                             |
| json_dumps              | 12.4 ms                                                | 9.46 ms: 1.31x faster                                                            |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                             |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                                            |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.01 ms: 1.14x faster                                                            |
| genshi_xml              | 51.4 ms                                                | 46.5 ms: 1.11x faster                                                            |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                                           |
| richards                | 46.1 ms                                                | 42.3 ms: 1.09x faster                                                            |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                                             |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                                            |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                             |
| html5lib                | 64.8 ms                                                | 60.2 ms: 1.08x faster                                                            |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.07x faster                                                             |
| logging_silent          | 98.0 ns                                                | 91.5 ns: 1.07x faster                                                            |
| deepcopy_memo           | 35.8 us                                                | 33.5 us: 1.07x faster                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.07x faster                                                           |
| hexiom                  | 6.34 ms                                                | 5.95 ms: 1.07x faster                                                            |
| mdp                     | 2.63 sec                                               | 2.47 sec: 1.07x faster                                                           |
| pyflate                 | 419 ms                                                 | 394 ms: 1.06x faster                                                             |
| float                   | 76.8 ms                                                | 72.2 ms: 1.06x faster                                                            |
| pprint_safe_repr        | 706 ms                                                 | 666 ms: 1.06x faster                                                             |
| coroutines              | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                            |
| scimark_monte_carlo     | 68.0 ms                                                | 64.3 ms: 1.06x faster                                                            |
| nqueens                 | 83.8 ms                                                | 79.4 ms: 1.05x faster                                                            |
| logging_simple          | 6.02 us                                                | 5.71 us: 1.05x faster                                                            |
| bench_thread_pool       | 817 us                                                 | 778 us: 1.05x faster                                                             |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                             |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                                             |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                            |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                            |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                             |
| deepcopy_reduce         | 3.02 us                                                | 2.89 us: 1.04x faster                                                            |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                             |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                             |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                             |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                            |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                                            |
| dulwich_log             | 64.0 ms                                                | 61.6 ms: 1.04x faster                                                            |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                                           |
| sympy_str               | 291 ms                                                 | 281 ms: 1.03x faster                                                             |
| unpack_sequence         | 44.5 ns                                                | 43.0 ns: 1.03x faster                                                            |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                            |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                                            |
| tornado_http            | 96.5 ms                                                | 93.4 ms: 1.03x faster                                                            |
| telco                   | 6.43 ms                                                | 6.24 ms: 1.03x faster                                                            |
| json                    | 4.87 ms                                                | 4.72 ms: 1.03x faster                                                            |
| deepcopy                | 341 us                                                 | 332 us: 1.03x faster                                                             |
| chaos                   | 68.7 ms                                                | 66.9 ms: 1.03x faster                                                            |
| logging_format          | 6.48 us                                                | 6.31 us: 1.03x faster                                                            |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                             |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                            |
| thrift                  | 760 us                                                 | 746 us: 1.02x faster                                                             |
| crypto_pyaes            | 75.7 ms                                                | 74.3 ms: 1.02x faster                                                            |
| pickle_dict             | 31.2 us                                                | 30.7 us: 1.02x faster                                                            |
| raytrace                | 291 ms                                                 | 287 ms: 1.01x faster                                                             |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                                             |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                            |
| pickle_list             | 4.14 us                                                | 4.10 us: 1.01x faster                                                            |
| mako                    | 9.83 ms                                                | 9.75 ms: 1.01x faster                                                            |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                             |
| gc_traversal            | 3.82 ms                                                | 3.79 ms: 1.01x faster                                                            |
| python_startup          | 8.58 ms                                                | 8.57 ms: 1.00x faster                                                            |
| async_tree_cpu_io_mixed | 736 ms                                                 | 745 ms: 1.01x slower                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                                             |
| python_startup_no_site  | 6.04 ms                                                | 6.13 ms: 1.01x slower                                                            |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                           |
| xml_etree_generate      | 75.9 ms                                                | 77.5 ms: 1.02x slower                                                            |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                            |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.02x slower                                                            |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                            |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                             |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                                            |
| regex_effbot            | 3.46 ms                                                | 3.58 ms: 1.03x slower                                                            |
| nbody                   | 90.0 ms                                                | 93.7 ms: 1.04x slower                                                            |
| async_tree_memoization  | 624 ms                                                 | 656 ms: 1.05x slower                                                             |
| generators              | 73.5 ms                                                | 77.2 ms: 1.05x slower                                                            |
| dask                    | 365 ms                                                 | 496 ms: 1.36x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (12): unpickle, async_tree_none, spectral_norm, django_template, unpickle_list, scimark_lu, async_generators, chameleon, bench_mp_pool, xml_etree_process, coverage, djangocms
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-df06ef8/bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8.json: mypy
