
# Results vs. base

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 57469f4
- commit date: 2023-01-28
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 254 ms: 1.01x slower                                                       |
| tornado_http   | 93.7 ms                                                                | 94.3 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (3): chameleon, docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 72.1 ms                                                                | 75.1 ms: 1.04x slower                                                      |
| nbody          | 92.9 ms                                                                | 92.3 ms: 1.01x faster                                                      |
| pidigits       | 198 ms                                                                 | 192 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 131 ms: 1.02x slower                                                       |
| regex_dna      | 210 ms                                                                 | 219 ms: 1.04x slower                                                       |
| regex_effbot   | 3.48 ms                                                                | 3.60 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.46 ms                                                                | 9.40 ms: 1.01x faster                                                      |
| json_loads           | 24.1 us                                                                | 23.9 us: 1.01x faster                                                      |
| pickle               | 9.90 us                                                                | 9.98 us: 1.01x slower                                                      |
| pickle_dict          | 30.1 us                                                                | 30.8 us: 1.02x slower                                                      |
| pickle_list          | 4.00 us                                                                | 4.06 us: 1.02x slower                                                      |
| pickle_pure_python   | 284 us                                                                 | 292 us: 1.03x slower                                                       |
| unpickle_list        | 5.01 us                                                                | 5.07 us: 1.01x slower                                                      |
| unpickle_pure_python | 196 us                                                                 | 208 us: 1.06x slower                                                       |
| xml_etree_generate   | 78.6 ms                                                                | 77.5 ms: 1.01x faster                                                      |
| xml_etree_process    | 54.2 ms                                                                | 53.6 ms: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (3): unpickle, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.93 ms                                                                | 8.70 ms: 1.03x faster                                                      |
| python_startup_no_site | 6.46 ms                                                                | 6.23 ms: 1.04x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 32.6 ms                                                                | 32.4 ms: 1.00x faster                                                      |
| genshi_xml      | 47.2 ms                                                                | 46.4 ms: 1.02x faster                                                      |
| mako            | 9.61 ms                                                                | 9.44 ms: 1.02x faster                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark              | bm-20230126-linux-x86_64-python-8d18d1ffd52eb3917c45-3.12.0a4+-8d18d1f | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3                   | 251 ms                                                                 | 254 ms: 1.01x slower                                                       |
| aiohttp                | 997 us                                                                 | 1.00 ms: 1.00x slower                                                      |
| async_tree_io          | 1.31 sec                                                               | 1.30 sec: 1.01x faster                                                     |
| async_tree_memoization | 616 ms                                                                 | 661 ms: 1.07x slower                                                       |
| chaos                  | 64.0 ms                                                                | 65.9 ms: 1.03x slower                                                      |
| bench_thread_pool      | 776 us                                                                 | 783 us: 1.01x slower                                                       |
| coroutines             | 25.0 ms                                                                | 26.0 ms: 1.04x slower                                                      |
| coverage               | 96.2 ms                                                                | 102 ms: 1.06x slower                                                       |
| crypto_pyaes           | 73.8 ms                                                                | 72.6 ms: 1.02x faster                                                      |
| dask                   | 496 ms                                                                 | 511 ms: 1.03x slower                                                       |
| deepcopy               | 328 us                                                                 | 324 us: 1.01x faster                                                       |
| deepcopy_memo          | 34.3 us                                                                | 34.0 us: 1.01x faster                                                      |
| deltablue              | 3.24 ms                                                                | 3.35 ms: 1.04x slower                                                      |
| django_template        | 32.6 ms                                                                | 32.4 ms: 1.00x faster                                                      |
| dulwich_log            | 62.2 ms                                                                | 62.9 ms: 1.01x slower                                                      |
| fannkuch               | 363 ms                                                                 | 385 ms: 1.06x slower                                                       |
| float                  | 72.1 ms                                                                | 75.1 ms: 1.04x slower                                                      |
| gc_traversal           | 4.16 ms                                                                | 3.76 ms: 1.11x faster                                                      |
| generators             | 75.0 ms                                                                | 74.4 ms: 1.01x faster                                                      |
| genshi_xml             | 47.2 ms                                                                | 46.4 ms: 1.02x faster                                                      |
| go                     | 136 ms                                                                 | 140 ms: 1.03x slower                                                       |
| hexiom                 | 5.98 ms                                                                | 6.16 ms: 1.03x slower                                                      |
| json_dumps             | 9.46 ms                                                                | 9.40 ms: 1.01x faster                                                      |
| json_loads             | 24.1 us                                                                | 23.9 us: 1.01x faster                                                      |
| logging_format         | 6.33 us                                                                | 6.37 us: 1.01x slower                                                      |
| mako                   | 9.61 ms                                                                | 9.44 ms: 1.02x faster                                                      |
| mdp                    | 2.61 sec                                                               | 2.45 sec: 1.06x faster                                                     |
| meteor_contest         | 108 ms                                                                 | 105 ms: 1.03x faster                                                       |
| nbody                  | 92.9 ms                                                                | 92.3 ms: 1.01x faster                                                      |
| nqueens                | 75.4 ms                                                                | 78.0 ms: 1.03x slower                                                      |
| pathlib                | 17.9 ms                                                                | 17.6 ms: 1.02x faster                                                      |
| pickle                 | 9.90 us                                                                | 9.98 us: 1.01x slower                                                      |
| pickle_dict            | 30.1 us                                                                | 30.8 us: 1.02x slower                                                      |
| pickle_list            | 4.00 us                                                                | 4.06 us: 1.02x slower                                                      |
| pickle_pure_python     | 284 us                                                                 | 292 us: 1.03x slower                                                       |
| pidigits               | 198 ms                                                                 | 192 ms: 1.03x faster                                                       |
| pprint_safe_repr       | 671 ms                                                                 | 681 ms: 1.01x slower                                                       |
| pprint_pformat         | 1.38 sec                                                               | 1.41 sec: 1.02x slower                                                     |
| pycparser              | 1.14 sec                                                               | 1.16 sec: 1.01x slower                                                     |
| pyflate                | 393 ms                                                                 | 432 ms: 1.10x slower                                                       |
| python_startup         | 8.93 ms                                                                | 8.70 ms: 1.03x faster                                                      |
| python_startup_no_site | 6.46 ms                                                                | 6.23 ms: 1.04x faster                                                      |
| regex_compile          | 129 ms                                                                 | 131 ms: 1.02x slower                                                       |
| regex_dna              | 210 ms                                                                 | 219 ms: 1.04x slower                                                       |
| regex_effbot           | 3.48 ms                                                                | 3.60 ms: 1.04x slower                                                      |
| richards               | 42.0 ms                                                                | 42.9 ms: 1.02x slower                                                      |
| scimark_fft            | 297 ms                                                                 | 302 ms: 1.02x slower                                                       |
| scimark_lu             | 106 ms                                                                 | 105 ms: 1.01x faster                                                       |
| scimark_monte_carlo    | 66.8 ms                                                                | 67.3 ms: 1.01x slower                                                      |
| scimark_sor            | 106 ms                                                                 | 118 ms: 1.12x slower                                                       |
| spectral_norm          | 94.4 ms                                                                | 96.1 ms: 1.02x slower                                                      |
| sqlglot_parse          | 1.40 ms                                                                | 1.43 ms: 1.02x slower                                                      |
| sqlglot_transpile      | 1.69 ms                                                                | 1.72 ms: 1.02x slower                                                      |
| sqlglot_optimize       | 50.6 ms                                                                | 51.0 ms: 1.01x slower                                                      |
| sqlglot_normalize      | 104 ms                                                                 | 105 ms: 1.01x slower                                                       |
| sympy_expand           | 451 ms                                                                 | 454 ms: 1.01x slower                                                       |
| sympy_integrate        | 19.7 ms                                                                | 20.0 ms: 1.01x slower                                                      |
| telco                  | 6.24 ms                                                                | 6.34 ms: 1.02x slower                                                      |
| tornado_http           | 93.7 ms                                                                | 94.3 ms: 1.01x slower                                                      |
| unpack_sequence        | 42.8 ns                                                                | 41.7 ns: 1.03x faster                                                      |
| unpickle_list          | 5.01 us                                                                | 5.07 us: 1.01x slower                                                      |
| unpickle_pure_python   | 196 us                                                                 | 208 us: 1.06x slower                                                       |
| xml_etree_generate     | 78.6 ms                                                                | 77.5 ms: 1.01x faster                                                      |
| xml_etree_process      | 54.2 ms                                                                | 53.6 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (27): async_generators, async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp, chameleon, bench_mp_pool, deepcopy_reduce, djangocms, docutils, create_gc_cycles, genshi_text, gunicorn, html5lib, json, logging_silent, logging_simple, mypy, raytrace, regex_v8, scimark_sparse_mat_mult, sqlite_synth, sympy_sum, sympy_str, thrift, unpickle, xml_etree_parse, xml_etree_iterparse
