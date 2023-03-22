
# Results vs. base

- fork: iritkatriel
- ref: remove_JUMP_IF_FALSE
- machine: linux-x86_64
- commit hash: b2bf829
- commit date: 2023-03-22
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 248 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (4): chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.7 ms                                                                | 87.1 ms: 1.01x faster                                                       |
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.9 ms                                                                | 21.8 ms: 1.01x faster                                                       |
| regex_dna      | 204 ms                                                                 | 203 ms: 1.00x faster                                                        |
| regex_compile  | 133 ms                                                                 | 133 ms: 1.00x slower                                                        |
| regex_effbot   | 3.42 ms                                                                | 3.43 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_list         | 4.23 us                                                                | 4.11 us: 1.03x faster                                                       |
| pickle              | 10.4 us                                                                | 10.2 us: 1.02x faster                                                       |
| json_dumps          | 9.59 ms                                                                | 9.46 ms: 1.01x faster                                                       |
| unpickle_list       | 5.05 us                                                                | 4.99 us: 1.01x faster                                                       |
| json_loads          | 24.2 us                                                                | 23.9 us: 1.01x faster                                                       |
| xml_etree_parse     | 151 ms                                                                 | 153 ms: 1.01x slower                                                        |
| xml_etree_iterparse | 102 ms                                                                 | 104 ms: 1.02x slower                                                        |
| pickle_dict         | 31.2 us                                                                | 31.9 us: 1.02x slower                                                       |
| unpickle            | 13.2 us                                                                | 13.8 us: 1.04x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.88 ms                                                                | 8.81 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.56 ms                                                                | 6.51 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 10.1 ms                                                                | 9.94 ms: 1.02x faster                                                       |
| genshi_xml     | 48.0 ms                                                                | 47.4 ms: 1.01x faster                                                       |
| genshi_text    | 21.5 ms                                                                | 21.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230321-linux-x86_64-python-d1a89ce5156cd4e1eff5-3.12.0a6+-d1a89ce | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 44.4 ns                                                                | 42.0 ns: 1.06x faster                                                       |
| scimark_sparse_mat_mult | 4.28 ms                                                                | 4.08 ms: 1.05x faster                                                       |
| mdp                     | 2.63 sec                                                               | 2.55 sec: 1.03x faster                                                      |
| pickle_list             | 4.23 us                                                                | 4.11 us: 1.03x faster                                                       |
| spectral_norm           | 92.0 ms                                                                | 89.6 ms: 1.03x faster                                                       |
| scimark_fft             | 303 ms                                                                 | 296 ms: 1.03x faster                                                        |
| deepcopy_memo           | 34.5 us                                                                | 33.7 us: 1.03x faster                                                       |
| generators              | 29.7 ms                                                                | 29.0 ms: 1.02x faster                                                       |
| scimark_monte_carlo     | 66.2 ms                                                                | 64.7 ms: 1.02x faster                                                       |
| pyflate                 | 416 ms                                                                 | 407 ms: 1.02x faster                                                        |
| pickle                  | 10.4 us                                                                | 10.2 us: 1.02x faster                                                       |
| mako                    | 10.1 ms                                                                | 9.94 ms: 1.02x faster                                                       |
| genshi_xml              | 48.0 ms                                                                | 47.4 ms: 1.01x faster                                                       |
| json_dumps              | 9.59 ms                                                                | 9.46 ms: 1.01x faster                                                       |
| deepcopy                | 330 us                                                                 | 326 us: 1.01x faster                                                        |
| deepcopy_reduce         | 2.95 us                                                                | 2.92 us: 1.01x faster                                                       |
| crypto_pyaes            | 74.9 ms                                                                | 74.1 ms: 1.01x faster                                                       |
| unpickle_list           | 5.05 us                                                                | 4.99 us: 1.01x faster                                                       |
| json_loads              | 24.2 us                                                                | 23.9 us: 1.01x faster                                                       |
| 2to3                    | 251 ms                                                                 | 248 ms: 1.01x faster                                                        |
| hexiom                  | 6.17 ms                                                                | 6.11 ms: 1.01x faster                                                       |
| async_generators        | 417 ms                                                                 | 413 ms: 1.01x faster                                                        |
| python_startup          | 8.88 ms                                                                | 8.81 ms: 1.01x faster                                                       |
| python_startup_no_site  | 6.56 ms                                                                | 6.51 ms: 1.01x faster                                                       |
| nbody                   | 87.7 ms                                                                | 87.1 ms: 1.01x faster                                                       |
| chaos                   | 65.8 ms                                                                | 65.4 ms: 1.01x faster                                                       |
| regex_v8                | 21.9 ms                                                                | 21.8 ms: 1.01x faster                                                       |
| regex_dna               | 204 ms                                                                 | 203 ms: 1.00x faster                                                        |
| sympy_integrate         | 20.5 ms                                                                | 20.4 ms: 1.00x faster                                                       |
| pidigits                | 189 ms                                                                 | 189 ms: 1.00x slower                                                        |
| bench_thread_pool       | 788 us                                                                 | 790 us: 1.00x slower                                                        |
| regex_compile           | 133 ms                                                                 | 133 ms: 1.00x slower                                                        |
| regex_effbot            | 3.42 ms                                                                | 3.43 ms: 1.00x slower                                                       |
| asyncio_tcp             | 504 ms                                                                 | 506 ms: 1.00x slower                                                        |
| sympy_str               | 282 ms                                                                 | 283 ms: 1.00x slower                                                        |
| dulwich_log             | 63.0 ms                                                                | 63.3 ms: 1.00x slower                                                       |
| sympy_expand            | 456 ms                                                                 | 459 ms: 1.01x slower                                                        |
| pprint_safe_repr        | 691 ms                                                                 | 695 ms: 1.01x slower                                                        |
| genshi_text             | 21.5 ms                                                                | 21.7 ms: 1.01x slower                                                       |
| sqlglot_optimize        | 50.9 ms                                                                | 51.4 ms: 1.01x slower                                                       |
| raytrace                | 281 ms                                                                 | 284 ms: 1.01x slower                                                        |
| meteor_contest          | 103 ms                                                                 | 104 ms: 1.01x slower                                                        |
| thrift                  | 771 us                                                                 | 780 us: 1.01x slower                                                        |
| fannkuch                | 368 ms                                                                 | 372 ms: 1.01x slower                                                        |
| deltablue               | 3.17 ms                                                                | 3.21 ms: 1.01x slower                                                       |
| comprehensions          | 23.4 us                                                                | 23.7 us: 1.01x slower                                                       |
| xml_etree_parse         | 151 ms                                                                 | 153 ms: 1.01x slower                                                        |
| pycparser               | 1.11 sec                                                               | 1.12 sec: 1.01x slower                                                      |
| nqueens                 | 79.7 ms                                                                | 80.9 ms: 1.01x slower                                                       |
| richards                | 43.2 ms                                                                | 43.9 ms: 1.02x slower                                                       |
| sqlglot_transpile       | 1.72 ms                                                                | 1.75 ms: 1.02x slower                                                       |
| sqlglot_parse           | 1.43 ms                                                                | 1.45 ms: 1.02x slower                                                       |
| xml_etree_iterparse     | 102 ms                                                                 | 104 ms: 1.02x slower                                                        |
| logging_silent          | 94.8 ns                                                                | 96.6 ns: 1.02x slower                                                       |
| sqlalchemy_declarative  | 136 ms                                                                 | 139 ms: 1.02x slower                                                        |
| pprint_pformat          | 1.40 sec                                                               | 1.43 sec: 1.02x slower                                                      |
| logging_format          | 6.26 us                                                                | 6.41 us: 1.02x slower                                                       |
| pickle_dict             | 31.2 us                                                                | 31.9 us: 1.02x slower                                                       |
| coverage                | 93.4 ms                                                                | 95.9 ms: 1.03x slower                                                       |
| gc_traversal            | 3.84 ms                                                                | 3.98 ms: 1.04x slower                                                       |
| unpickle                | 13.2 us                                                                | 13.8 us: 1.04x slower                                                       |
| logging_simple          | 5.62 us                                                                | 5.87 us: 1.04x slower                                                       |
| async_tree_memoization  | 624 ms                                                                 | 653 ms: 1.05x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (31): json, float, djangocms, go, sqlalchemy_imperative, xml_etree_generate, sqlite_synth, scimark_sor, unpickle_pure_python, aiohttp, mypy2, create_gc_cycles, pathlib, sympy_sum, bench_mp_pool, docutils, async_tree_io, telco, gunicorn, coroutines, xml_etree_process, async_tree_none, sqlglot_normalize, pickle_pure_python, tornado_http, django_template, dask, html5lib, scimark_lu, chameleon, async_tree_cpu_io_mixed
