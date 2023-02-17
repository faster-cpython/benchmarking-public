
# Results vs. base

- fork: brandtbucher
- ref: replicate_load_fast
- machine: linux-x86_64
- commit hash: 7dd73c5
- commit date: 2023-02-16
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| chameleon      | 6.48 ms                                                                | 6.34 ms: 1.02x faster                                                       |
| docutils       | 2.53 sec                                                               | 2.57 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 74.1 ms                                                                | 72.6 ms: 1.02x faster                                                       |
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x faster                                                        |
| nbody          | 91.4 ms                                                                | 93.2 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.8 ms                                                                | 21.6 ms: 1.01x faster                                                       |
| regex_compile  | 131 ms                                                                 | 132 ms: 1.01x slower                                                        |
| regex_dna      | 206 ms                                                                 | 208 ms: 1.01x slower                                                        |
| regex_effbot   | 3.59 ms                                                                | 3.67 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps          | 9.70 ms                                                                | 9.66 ms: 1.00x faster                                                       |
| xml_etree_iterparse | 101 ms                                                                 | 103 ms: 1.02x slower                                                        |
| xml_etree_process   | 55.4 ms                                                                | 56.5 ms: 1.02x slower                                                       |
| xml_etree_generate  | 80.6 ms                                                                | 82.5 ms: 1.02x slower                                                       |
| unpickle_list       | 4.98 us                                                                | 5.13 us: 1.03x slower                                                       |
| pickle              | 9.85 us                                                                | 10.2 us: 1.03x slower                                                       |
| pickle_dict         | 30.5 us                                                                | 31.8 us: 1.04x slower                                                       |
| pickle_list         | 4.03 us                                                                | 4.26 us: 1.06x slower                                                       |
| Geometric mean      | (ref)                                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (5): pickle_pure_python, unpickle_pure_python, xml_etree_parse, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 9.02 ms                                                                | 9.00 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.53 ms                                                                | 6.53 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.83 ms                                                                | 9.67 ms: 1.02x faster                                                       |
| genshi_xml      | 48.1 ms                                                                | 47.4 ms: 1.02x faster                                                       |
| django_template | 33.3 ms                                                                | 33.1 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark              | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                    | 2.67 sec                                                               | 2.49 sec: 1.07x faster                                                      |
| sqlite_synth           | 2.65 us                                                                | 2.58 us: 1.03x faster                                                       |
| sqlalchemy_declarative | 141 ms                                                                 | 138 ms: 1.03x faster                                                        |
| coverage               | 97.8 ms                                                                | 95.3 ms: 1.03x faster                                                       |
| scimark_lu             | 111 ms                                                                 | 108 ms: 1.02x faster                                                        |
| chameleon              | 6.48 ms                                                                | 6.34 ms: 1.02x faster                                                       |
| float                  | 74.1 ms                                                                | 72.6 ms: 1.02x faster                                                       |
| richards               | 43.2 ms                                                                | 42.3 ms: 1.02x faster                                                       |
| mako                   | 9.83 ms                                                                | 9.67 ms: 1.02x faster                                                       |
| genshi_xml             | 48.1 ms                                                                | 47.4 ms: 1.02x faster                                                       |
| deltablue              | 3.27 ms                                                                | 3.22 ms: 1.02x faster                                                       |
| scimark_monte_carlo    | 66.2 ms                                                                | 65.2 ms: 1.01x faster                                                       |
| create_gc_cycles       | 1.50 ms                                                                | 1.48 ms: 1.01x faster                                                       |
| coroutines             | 22.6 ms                                                                | 22.2 ms: 1.01x faster                                                       |
| logging_simple         | 5.76 us                                                                | 5.69 us: 1.01x faster                                                       |
| async_tree_io          | 1.33 sec                                                               | 1.31 sec: 1.01x faster                                                      |
| pycparser              | 1.12 sec                                                               | 1.10 sec: 1.01x faster                                                      |
| fannkuch               | 373 ms                                                                 | 368 ms: 1.01x faster                                                        |
| deepcopy_reduce        | 2.99 us                                                                | 2.96 us: 1.01x faster                                                       |
| sqlglot_parse          | 1.46 ms                                                                | 1.44 ms: 1.01x faster                                                       |
| sqlglot_transpile      | 1.75 ms                                                                | 1.74 ms: 1.01x faster                                                       |
| regex_v8               | 21.8 ms                                                                | 21.6 ms: 1.01x faster                                                       |
| logging_format         | 6.34 us                                                                | 6.28 us: 1.01x faster                                                       |
| bench_thread_pool      | 798 us                                                                 | 792 us: 1.01x faster                                                        |
| django_template        | 33.3 ms                                                                | 33.1 ms: 1.01x faster                                                       |
| json_dumps             | 9.70 ms                                                                | 9.66 ms: 1.00x faster                                                       |
| gunicorn               | 1.09 ms                                                                | 1.09 ms: 1.00x faster                                                       |
| python_startup         | 9.02 ms                                                                | 9.00 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.53 ms                                                                | 6.53 ms: 1.00x faster                                                       |
| pidigits               | 189 ms                                                                 | 189 ms: 1.00x faster                                                        |
| sympy_integrate        | 19.9 ms                                                                | 20.0 ms: 1.00x slower                                                       |
| deepcopy               | 334 us                                                                 | 335 us: 1.00x slower                                                        |
| pprint_pformat         | 1.41 sec                                                               | 1.41 sec: 1.00x slower                                                      |
| sympy_expand           | 458 ms                                                                 | 460 ms: 1.01x slower                                                        |
| thrift                 | 756 us                                                                 | 760 us: 1.01x slower                                                        |
| sympy_str              | 273 ms                                                                 | 275 ms: 1.01x slower                                                        |
| dulwich_log            | 63.5 ms                                                                | 63.9 ms: 1.01x slower                                                       |
| regex_compile          | 131 ms                                                                 | 132 ms: 1.01x slower                                                        |
| asyncio_tcp            | 502 ms                                                                 | 505 ms: 1.01x slower                                                        |
| regex_dna              | 206 ms                                                                 | 208 ms: 1.01x slower                                                        |
| nqueens                | 78.8 ms                                                                | 79.5 ms: 1.01x slower                                                       |
| mypy2                  | 332 ms                                                                 | 335 ms: 1.01x slower                                                        |
| raytrace               | 285 ms                                                                 | 288 ms: 1.01x slower                                                        |
| pprint_safe_repr       | 685 ms                                                                 | 692 ms: 1.01x slower                                                        |
| pyflate                | 401 ms                                                                 | 406 ms: 1.01x slower                                                        |
| gc_traversal           | 3.61 ms                                                                | 3.66 ms: 1.02x slower                                                       |
| crypto_pyaes           | 72.4 ms                                                                | 73.5 ms: 1.02x slower                                                       |
| xml_etree_iterparse    | 101 ms                                                                 | 103 ms: 1.02x slower                                                        |
| docutils               | 2.53 sec                                                               | 2.57 sec: 1.02x slower                                                      |
| chaos                  | 66.1 ms                                                                | 67.3 ms: 1.02x slower                                                       |
| hexiom                 | 6.12 ms                                                                | 6.24 ms: 1.02x slower                                                       |
| nbody                  | 91.4 ms                                                                | 93.2 ms: 1.02x slower                                                       |
| go                     | 135 ms                                                                 | 138 ms: 1.02x slower                                                        |
| regex_effbot           | 3.59 ms                                                                | 3.67 ms: 1.02x slower                                                       |
| xml_etree_process      | 55.4 ms                                                                | 56.5 ms: 1.02x slower                                                       |
| scimark_fft            | 306 ms                                                                 | 312 ms: 1.02x slower                                                        |
| xml_etree_generate     | 80.6 ms                                                                | 82.5 ms: 1.02x slower                                                       |
| unpickle_list          | 4.98 us                                                                | 5.13 us: 1.03x slower                                                       |
| pickle                 | 9.85 us                                                                | 10.2 us: 1.03x slower                                                       |
| pickle_dict            | 30.5 us                                                                | 31.8 us: 1.04x slower                                                       |
| telco                  | 6.29 ms                                                                | 6.55 ms: 1.04x slower                                                       |
| pickle_list            | 4.03 us                                                                | 4.26 us: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (31): async_tree_memoization, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, async_tree_none, unpack_sequence, genshi_text, sqlalchemy_imperative, djangocms, meteor_contest, sqlglot_normalize, spectral_norm, generators, 2to3, aiohttp, dask, bench_mp_pool, pickle_pure_python, tornado_http, html5lib, scimark_sor, sqlglot_optimize, sympy_sum, pathlib, async_generators, unpickle_pure_python, xml_etree_parse, json_loads, deepcopy_memo, json, logging_silent, unpickle
