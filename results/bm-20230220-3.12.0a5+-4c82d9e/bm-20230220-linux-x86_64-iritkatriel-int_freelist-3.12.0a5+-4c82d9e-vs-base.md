
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 4c82d9e
- commit date: 2023-02-20
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (4): 2to3, chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                 | 198 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 128 ms: 1.00x faster                                                |
| regex_v8       | 21.6 ms                                                                | 21.7 ms: 1.01x slower                                               |
| regex_dna      | 211 ms                                                                 | 216 ms: 1.02x slower                                                |
| regex_effbot   | 3.33 ms                                                                | 3.47 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|---------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list       | 5.00 us                                                                | 4.84 us: 1.03x faster                                               |
| json_loads          | 24.1 us                                                                | 23.7 us: 1.02x faster                                               |
| xml_etree_parse     | 149 ms                                                                 | 147 ms: 1.01x faster                                                |
| xml_etree_iterparse | 103 ms                                                                 | 102 ms: 1.01x faster                                                |
| xml_etree_process   | 55.2 ms                                                                | 54.8 ms: 1.01x faster                                               |
| pickle_pure_python  | 290 us                                                                 | 288 us: 1.01x faster                                                |
| json_dumps          | 9.54 ms                                                                | 9.64 ms: 1.01x slower                                               |
| pickle_list         | 3.98 us                                                                | 4.05 us: 1.02x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (5): unpickle, xml_etree_generate, unpickle_pure_python, pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.86 ms                                                                | 8.93 ms: 1.01x slower                                               |
| python_startup_no_site | 6.43 ms                                                                | 6.48 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 33.5 ms                                                                | 32.6 ms: 1.03x faster                                               |
| genshi_xml      | 47.4 ms                                                                | 46.9 ms: 1.01x faster                                               |
| mako            | 9.61 ms                                                                | 9.69 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                     | 2.68 sec                                                               | 2.48 sec: 1.08x faster                                              |
| spectral_norm           | 98.1 ms                                                                | 94.4 ms: 1.04x faster                                               |
| unpickle_list           | 5.00 us                                                                | 4.84 us: 1.03x faster                                               |
| django_template         | 33.5 ms                                                                | 32.6 ms: 1.03x faster                                               |
| json_loads              | 24.1 us                                                                | 23.7 us: 1.02x faster                                               |
| async_tree_cpu_io_mixed | 759 ms                                                                 | 748 ms: 1.02x faster                                                |
| deepcopy_reduce         | 2.98 us                                                                | 2.94 us: 1.01x faster                                               |
| scimark_fft             | 307 ms                                                                 | 303 ms: 1.01x faster                                                |
| pprint_safe_repr        | 684 ms                                                                 | 676 ms: 1.01x faster                                                |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                               |
| meteor_contest          | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| genshi_xml              | 47.4 ms                                                                | 46.9 ms: 1.01x faster                                               |
| sympy_sum               | 158 ms                                                                 | 156 ms: 1.01x faster                                                |
| xml_etree_parse         | 149 ms                                                                 | 147 ms: 1.01x faster                                                |
| xml_etree_iterparse     | 103 ms                                                                 | 102 ms: 1.01x faster                                                |
| sympy_str               | 273 ms                                                                 | 270 ms: 1.01x faster                                                |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| pycparser               | 1.10 sec                                                               | 1.10 sec: 1.01x faster                                              |
| xml_etree_process       | 55.2 ms                                                                | 54.8 ms: 1.01x faster                                               |
| pickle_pure_python      | 290 us                                                                 | 288 us: 1.01x faster                                                |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                              |
| async_generators        | 428 ms                                                                 | 426 ms: 1.00x faster                                                |
| aiohttp                 | 1.00 ms                                                                | 998 us: 1.00x faster                                                |
| regex_compile           | 129 ms                                                                 | 128 ms: 1.00x faster                                                |
| sympy_integrate         | 19.9 ms                                                                | 19.8 ms: 1.00x faster                                               |
| pidigits                | 198 ms                                                                 | 198 ms: 1.00x slower                                                |
| docutils                | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                              |
| regex_v8                | 21.6 ms                                                                | 21.7 ms: 1.01x slower                                               |
| hexiom                  | 5.97 ms                                                                | 6.01 ms: 1.01x slower                                               |
| sqlite_synth            | 2.58 us                                                                | 2.60 us: 1.01x slower                                               |
| scimark_sparse_mat_mult | 3.91 ms                                                                | 3.93 ms: 1.01x slower                                               |
| bench_thread_pool       | 781 us                                                                 | 786 us: 1.01x slower                                                |
| python_startup          | 8.86 ms                                                                | 8.93 ms: 1.01x slower                                               |
| logging_format          | 6.26 us                                                                | 6.31 us: 1.01x slower                                               |
| sympy_expand            | 458 ms                                                                 | 462 ms: 1.01x slower                                                |
| python_startup_no_site  | 6.43 ms                                                                | 6.48 ms: 1.01x slower                                               |
| mako                    | 9.61 ms                                                                | 9.69 ms: 1.01x slower                                               |
| create_gc_cycles        | 1.46 ms                                                                | 1.47 ms: 1.01x slower                                               |
| coverage                | 99.0 ms                                                                | 100.0 ms: 1.01x slower                                              |
| json_dumps              | 9.54 ms                                                                | 9.64 ms: 1.01x slower                                               |
| deltablue               | 3.17 ms                                                                | 3.21 ms: 1.01x slower                                               |
| deepcopy                | 331 us                                                                 | 335 us: 1.01x slower                                                |
| asyncio_tcp             | 490 ms                                                                 | 497 ms: 1.01x slower                                                |
| richards                | 41.5 ms                                                                | 42.1 ms: 1.01x slower                                               |
| pathlib                 | 17.6 ms                                                                | 17.9 ms: 1.02x slower                                               |
| crypto_pyaes            | 73.5 ms                                                                | 74.6 ms: 1.02x slower                                               |
| nqueens                 | 78.8 ms                                                                | 80.2 ms: 1.02x slower                                               |
| pickle_list             | 3.98 us                                                                | 4.05 us: 1.02x slower                                               |
| json                    | 4.59 ms                                                                | 4.68 ms: 1.02x slower                                               |
| sqlalchemy_imperative   | 17.8 ms                                                                | 18.2 ms: 1.02x slower                                               |
| deepcopy_memo           | 34.5 us                                                                | 35.2 us: 1.02x slower                                               |
| regex_dna               | 211 ms                                                                 | 216 ms: 1.02x slower                                                |
| fannkuch                | 364 ms                                                                 | 374 ms: 1.03x slower                                                |
| logging_silent          | 92.3 ns                                                                | 95.0 ns: 1.03x slower                                               |
| telco                   | 6.34 ms                                                                | 6.54 ms: 1.03x slower                                               |
| regex_effbot            | 3.33 ms                                                                | 3.47 ms: 1.04x slower                                               |
| gc_traversal            | 3.64 ms                                                                | 4.17 ms: 1.14x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (35): async_tree_memoization, async_tree_none, nbody, chameleon, sqlglot_transpile, logging_simple, sqlalchemy_declarative, go, scimark_monte_carlo, html5lib, sqlglot_parse, float, unpickle, bench_mp_pool, async_tree_io, xml_etree_generate, coroutines, mypy2, tornado_http, 2to3, sqlglot_optimize, generators, scimark_sor, unpickle_pure_python, dulwich_log, thrift, pyflate, chaos, unpack_sequence, genshi_text, raytrace, pickle_dict, djangocms, scimark_lu, pickle
