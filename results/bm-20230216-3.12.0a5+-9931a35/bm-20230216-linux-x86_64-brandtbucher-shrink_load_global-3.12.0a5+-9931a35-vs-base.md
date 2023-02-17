
# Results vs. base

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: 9931a35
- commit date: 2023-02-16
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 248 ms                                                                 | 246 ms: 1.01x faster                                                       |
| docutils       | 2.53 sec                                                               | 2.54 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 74.1 ms                                                                | 72.9 ms: 1.02x faster                                                      |
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x faster                                                       |
| nbody          | 91.4 ms                                                                | 94.4 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 131 ms                                                                 | 129 ms: 1.01x faster                                                       |
| regex_v8       | 21.8 ms                                                                | 21.7 ms: 1.01x faster                                                      |
| regex_effbot   | 3.59 ms                                                                | 3.70 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.70 ms                                                                | 9.64 ms: 1.01x faster                                                      |
| unpickle_pure_python | 199 us                                                                 | 198 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                                 | 102 ms: 1.02x slower                                                       |
| xml_etree_generate   | 80.6 ms                                                                | 81.9 ms: 1.02x slower                                                      |
| unpickle_list        | 4.98 us                                                                | 5.06 us: 1.02x slower                                                      |
| xml_etree_process    | 55.4 ms                                                                | 56.3 ms: 1.02x slower                                                      |
| pickle               | 9.85 us                                                                | 10.1 us: 1.03x slower                                                      |
| pickle_dict          | 30.5 us                                                                | 31.7 us: 1.04x slower                                                      |
| pickle_list          | 4.03 us                                                                | 4.26 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.53 ms                                                                | 6.49 ms: 1.01x faster                                                      |
| python_startup         | 9.02 ms                                                                | 8.96 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 33.3 ms                                                                | 33.1 ms: 1.01x faster                                                      |
| genshi_text     | 21.2 ms                                                                | 21.3 ms: 1.01x slower                                                      |
| mako            | 9.83 ms                                                                | 10.0 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20230216-linux-x86_64-python-4d8959b73ac194ca9a2f-3.12.0a5+-4d8959b | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| richards               | 43.2 ms                                                                | 42.2 ms: 1.02x faster                                                      |
| pycparser              | 1.12 sec                                                               | 1.09 sec: 1.02x faster                                                     |
| deltablue              | 3.27 ms                                                                | 3.20 ms: 1.02x faster                                                      |
| sqlalchemy_declarative | 141 ms                                                                 | 138 ms: 1.02x faster                                                       |
| gunicorn               | 1.09 ms                                                                | 1.07 ms: 1.02x faster                                                      |
| create_gc_cycles       | 1.50 ms                                                                | 1.47 ms: 1.02x faster                                                      |
| async_tree_memoization | 656 ms                                                                 | 644 ms: 1.02x faster                                                       |
| float                  | 74.1 ms                                                                | 72.9 ms: 1.02x faster                                                      |
| scimark_lu             | 111 ms                                                                 | 109 ms: 1.01x faster                                                       |
| sqlglot_parse          | 1.46 ms                                                                | 1.44 ms: 1.01x faster                                                      |
| sympy_sum              | 160 ms                                                                 | 157 ms: 1.01x faster                                                       |
| async_tree_io          | 1.33 sec                                                               | 1.31 sec: 1.01x faster                                                     |
| sqlglot_transpile      | 1.75 ms                                                                | 1.73 ms: 1.01x faster                                                      |
| dulwich_log            | 63.5 ms                                                                | 62.9 ms: 1.01x faster                                                      |
| coverage               | 97.8 ms                                                                | 96.8 ms: 1.01x faster                                                      |
| regex_compile          | 131 ms                                                                 | 129 ms: 1.01x faster                                                       |
| sympy_str              | 273 ms                                                                 | 271 ms: 1.01x faster                                                       |
| sqlglot_normalize      | 105 ms                                                                 | 104 ms: 1.01x faster                                                       |
| bench_thread_pool      | 798 us                                                                 | 792 us: 1.01x faster                                                       |
| sqlite_synth           | 2.65 us                                                                | 2.63 us: 1.01x faster                                                      |
| 2to3                   | 248 ms                                                                 | 246 ms: 1.01x faster                                                       |
| json_dumps             | 9.70 ms                                                                | 9.64 ms: 1.01x faster                                                      |
| pprint_safe_repr       | 685 ms                                                                 | 681 ms: 1.01x faster                                                       |
| deepcopy_reduce        | 2.99 us                                                                | 2.98 us: 1.01x faster                                                      |
| python_startup_no_site | 6.53 ms                                                                | 6.49 ms: 1.01x faster                                                      |
| regex_v8               | 21.8 ms                                                                | 21.7 ms: 1.01x faster                                                      |
| aiohttp                | 1.01 ms                                                                | 1.00 ms: 1.01x faster                                                      |
| django_template        | 33.3 ms                                                                | 33.1 ms: 1.01x faster                                                      |
| python_startup         | 9.02 ms                                                                | 8.96 ms: 1.01x faster                                                      |
| unpickle_pure_python   | 199 us                                                                 | 198 us: 1.01x faster                                                       |
| pprint_pformat         | 1.41 sec                                                               | 1.40 sec: 1.01x faster                                                     |
| sympy_expand           | 458 ms                                                                 | 455 ms: 1.01x faster                                                       |
| mypy2                  | 332 ms                                                                 | 330 ms: 1.01x faster                                                       |
| pidigits               | 189 ms                                                                 | 189 ms: 1.00x faster                                                       |
| logging_format         | 6.34 us                                                                | 6.37 us: 1.00x slower                                                      |
| mdp                    | 2.67 sec                                                               | 2.68 sec: 1.00x slower                                                     |
| pathlib                | 17.9 ms                                                                | 18.0 ms: 1.00x slower                                                      |
| docutils               | 2.53 sec                                                               | 2.54 sec: 1.01x slower                                                     |
| asyncio_tcp            | 502 ms                                                                 | 504 ms: 1.01x slower                                                       |
| async_generators       | 410 ms                                                                 | 412 ms: 1.01x slower                                                       |
| go                     | 135 ms                                                                 | 136 ms: 1.01x slower                                                       |
| genshi_text            | 21.2 ms                                                                | 21.3 ms: 1.01x slower                                                      |
| raytrace               | 285 ms                                                                 | 287 ms: 1.01x slower                                                       |
| logging_simple         | 5.76 us                                                                | 5.82 us: 1.01x slower                                                      |
| chaos                  | 66.1 ms                                                                | 66.7 ms: 1.01x slower                                                      |
| spectral_norm          | 94.0 ms                                                                | 94.9 ms: 1.01x slower                                                      |
| deepcopy               | 334 us                                                                 | 337 us: 1.01x slower                                                       |
| json                   | 4.55 ms                                                                | 4.60 ms: 1.01x slower                                                      |
| scimark_fft            | 306 ms                                                                 | 309 ms: 1.01x slower                                                       |
| thrift                 | 756 us                                                                 | 766 us: 1.01x slower                                                       |
| gc_traversal           | 3.61 ms                                                                | 3.66 ms: 1.01x slower                                                      |
| telco                  | 6.29 ms                                                                | 6.38 ms: 1.01x slower                                                      |
| xml_etree_iterparse    | 101 ms                                                                 | 102 ms: 1.02x slower                                                       |
| xml_etree_generate     | 80.6 ms                                                                | 81.9 ms: 1.02x slower                                                      |
| unpickle_list          | 4.98 us                                                                | 5.06 us: 1.02x slower                                                      |
| crypto_pyaes           | 72.4 ms                                                                | 73.6 ms: 1.02x slower                                                      |
| xml_etree_process      | 55.4 ms                                                                | 56.3 ms: 1.02x slower                                                      |
| mako                   | 9.83 ms                                                                | 10.0 ms: 1.02x slower                                                      |
| nqueens                | 78.8 ms                                                                | 80.5 ms: 1.02x slower                                                      |
| logging_silent         | 93.4 ns                                                                | 95.8 ns: 1.02x slower                                                      |
| pickle                 | 9.85 us                                                                | 10.1 us: 1.03x slower                                                      |
| regex_effbot           | 3.59 ms                                                                | 3.70 ms: 1.03x slower                                                      |
| nbody                  | 91.4 ms                                                                | 94.4 ms: 1.03x slower                                                      |
| pickle_dict            | 30.5 us                                                                | 31.7 us: 1.04x slower                                                      |
| pickle_list            | 4.03 us                                                                | 4.26 us: 1.06x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (28): html5lib, async_tree_none, dask, async_tree_cpu_io_mixed, xml_etree_parse, fannkuch, scimark_sor, tornado_http, scimark_monte_carlo, sympy_integrate, sqlalchemy_imperative, generators, sqlglot_optimize, pickle_pure_python, hexiom, regex_dna, bench_mp_pool, unpack_sequence, deepcopy_memo, coroutines, scimark_sparse_mat_mult, pyflate, meteor_contest, genshi_xml, chameleon, json_loads, djangocms, unpickle
