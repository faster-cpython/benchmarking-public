
# Results vs. base

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: afbac86
- commit date: 2023-01-17
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 251 ms: 1.00x faster                                                        |
| docutils       | 2.51 sec                                                               | 2.48 sec: 1.01x faster                                                      |
| tornado_http   | 93.7 ms                                                                | 94.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.9 ms                                                                | 94.1 ms: 1.01x slower                                                       |
| pidigits       | 198 ms                                                                 | 197 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 128 ms: 1.01x faster                                                        |
| regex_effbot   | 3.48 ms                                                                | 3.52 ms: 1.01x slower                                                       |
| regex_v8       | 22.6 ms                                                                | 22.5 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.46 ms                                                                | 9.36 ms: 1.01x faster                                                       |
| json_loads           | 24.1 us                                                                | 23.8 us: 1.02x faster                                                       |
| pickle               | 9.90 us                                                                | 10.1 us: 1.02x slower                                                       |
| pickle_dict          | 30.1 us                                                                | 30.9 us: 1.03x slower                                                       |
| pickle_list          | 4.00 us                                                                | 4.10 us: 1.02x slower                                                       |
| pickle_pure_python   | 284 us                                                                 | 288 us: 1.01x slower                                                        |
| unpickle_list        | 5.01 us                                                                | 5.24 us: 1.04x slower                                                       |
| unpickle_pure_python | 196 us                                                                 | 201 us: 1.03x slower                                                        |
| xml_etree_iterparse  | 106 ms                                                                 | 102 ms: 1.04x faster                                                        |
| xml_etree_generate   | 78.6 ms                                                                | 77.2 ms: 1.02x faster                                                       |
| xml_etree_process    | 54.2 ms                                                                | 53.9 ms: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.93 ms                                                                | 8.84 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.46 ms                                                                | 6.39 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 32.6 ms                                                                | 32.4 ms: 1.01x faster                                                       |
| genshi_text     | 20.6 ms                                                                | 21.1 ms: 1.02x slower                                                       |
| mako            | 9.61 ms                                                                | 9.75 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3                   | 251 ms                                                                 | 251 ms: 1.00x faster                                                        |
| aiohttp                | 997 us                                                                 | 993 us: 1.00x faster                                                        |
| async_generators       | 354 ms                                                                 | 351 ms: 1.01x faster                                                        |
| async_tree_memoization | 616 ms                                                                 | 646 ms: 1.05x slower                                                        |
| asyncio_tcp            | 497 ms                                                                 | 499 ms: 1.00x slower                                                        |
| chaos                  | 64.0 ms                                                                | 64.2 ms: 1.00x slower                                                       |
| bench_thread_pool      | 776 us                                                                 | 778 us: 1.00x slower                                                        |
| coroutines             | 25.0 ms                                                                | 24.5 ms: 1.02x faster                                                       |
| coverage               | 96.2 ms                                                                | 93.5 ms: 1.03x faster                                                       |
| crypto_pyaes           | 73.8 ms                                                                | 72.2 ms: 1.02x faster                                                       |
| deepcopy_reduce        | 2.90 us                                                                | 2.93 us: 1.01x slower                                                       |
| django_template        | 32.6 ms                                                                | 32.4 ms: 1.01x faster                                                       |
| docutils               | 2.51 sec                                                               | 2.48 sec: 1.01x faster                                                      |
| dulwich_log            | 62.2 ms                                                                | 62.4 ms: 1.00x slower                                                       |
| create_gc_cycles       | 1.45 ms                                                                | 1.44 ms: 1.01x faster                                                       |
| gc_traversal           | 4.16 ms                                                                | 3.81 ms: 1.09x faster                                                       |
| generators             | 75.0 ms                                                                | 77.0 ms: 1.03x slower                                                       |
| genshi_text            | 20.6 ms                                                                | 21.1 ms: 1.02x slower                                                       |
| go                     | 136 ms                                                                 | 135 ms: 1.01x faster                                                        |
| gunicorn               | 1.07 ms                                                                | 1.06 ms: 1.01x faster                                                       |
| hexiom                 | 5.98 ms                                                                | 6.13 ms: 1.02x slower                                                       |
| json                   | 4.63 ms                                                                | 4.55 ms: 1.02x faster                                                       |
| json_dumps             | 9.46 ms                                                                | 9.36 ms: 1.01x faster                                                       |
| json_loads             | 24.1 us                                                                | 23.8 us: 1.02x faster                                                       |
| logging_format         | 6.33 us                                                                | 6.42 us: 1.01x slower                                                       |
| logging_simple         | 5.73 us                                                                | 5.83 us: 1.02x slower                                                       |
| mako                   | 9.61 ms                                                                | 9.75 ms: 1.01x slower                                                       |
| meteor_contest         | 108 ms                                                                 | 105 ms: 1.03x faster                                                        |
| nbody                  | 92.9 ms                                                                | 94.1 ms: 1.01x slower                                                       |
| nqueens                | 75.4 ms                                                                | 76.3 ms: 1.01x slower                                                       |
| pickle                 | 9.90 us                                                                | 10.1 us: 1.02x slower                                                       |
| pickle_dict            | 30.1 us                                                                | 30.9 us: 1.03x slower                                                       |
| pickle_list            | 4.00 us                                                                | 4.10 us: 1.02x slower                                                       |
| pickle_pure_python     | 284 us                                                                 | 288 us: 1.01x slower                                                        |
| pidigits               | 198 ms                                                                 | 197 ms: 1.00x faster                                                        |
| pprint_safe_repr       | 671 ms                                                                 | 677 ms: 1.01x slower                                                        |
| pprint_pformat         | 1.38 sec                                                               | 1.38 sec: 1.01x slower                                                      |
| pyflate                | 393 ms                                                                 | 414 ms: 1.06x slower                                                        |
| python_startup         | 8.93 ms                                                                | 8.84 ms: 1.01x faster                                                       |
| python_startup_no_site | 6.46 ms                                                                | 6.39 ms: 1.01x faster                                                       |
| regex_compile          | 129 ms                                                                 | 128 ms: 1.01x faster                                                        |
| regex_effbot           | 3.48 ms                                                                | 3.52 ms: 1.01x slower                                                       |
| regex_v8               | 22.6 ms                                                                | 22.5 ms: 1.00x faster                                                       |
| richards               | 42.0 ms                                                                | 42.4 ms: 1.01x slower                                                       |
| scimark_fft            | 297 ms                                                                 | 302 ms: 1.02x slower                                                        |
| scimark_lu             | 106 ms                                                                 | 108 ms: 1.01x slower                                                        |
| sqlglot_parse          | 1.40 ms                                                                | 1.41 ms: 1.01x slower                                                       |
| sqlglot_optimize       | 50.6 ms                                                                | 51.0 ms: 1.01x slower                                                       |
| sqlglot_normalize      | 104 ms                                                                 | 105 ms: 1.01x slower                                                        |
| sympy_expand           | 451 ms                                                                 | 454 ms: 1.01x slower                                                        |
| sympy_sum              | 155 ms                                                                 | 155 ms: 1.01x faster                                                        |
| telco                  | 6.24 ms                                                                | 6.45 ms: 1.03x slower                                                       |
| thrift                 | 746 us                                                                 | 737 us: 1.01x faster                                                        |
| tornado_http           | 93.7 ms                                                                | 94.3 ms: 1.01x slower                                                       |
| unpack_sequence        | 42.8 ns                                                                | 43.2 ns: 1.01x slower                                                       |
| unpickle_list          | 5.01 us                                                                | 5.24 us: 1.04x slower                                                       |
| unpickle_pure_python   | 196 us                                                                 | 201 us: 1.03x slower                                                        |
| xml_etree_iterparse    | 106 ms                                                                 | 102 ms: 1.04x faster                                                        |
| xml_etree_generate     | 78.6 ms                                                                | 77.2 ms: 1.02x faster                                                       |
| xml_etree_process      | 54.2 ms                                                                | 53.9 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                |

Benchmark hidden because not significant (31): async_tree_none, async_tree_cpu_io_mixed, async_tree_io, chameleon, bench_mp_pool, dask, deepcopy, deepcopy_memo, deltablue, djangocms, fannkuch, float, genshi_xml, html5lib, logging_silent, mdp, mypy, pathlib, pycparser, raytrace, regex_dna, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sqlglot_transpile, sqlite_synth, sympy_integrate, sympy_str, unpickle, xml_etree_parse
