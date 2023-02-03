
# Results vs. base

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: fa5965d
- commit date: 2023-02-02
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230202-linux-x86_64-python-5dcae3f0c3e907225121-3.12.0a4+-5dcae3f | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 251 ms: 1.01x faster                                                       |
| chameleon      | 6.34 ms                                                                | 6.26 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230202-linux-x86_64-python-5dcae3f0c3e907225121-3.12.0a4+-5dcae3f | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 72.2 ms                                                                | 71.9 ms: 1.00x faster                                                      |
| pidigits       | 189 ms                                                                 | 198 ms: 1.04x slower                                                       |
| nbody          | 94.5 ms                                                                | 98.9 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230202-linux-x86_64-python-5dcae3f0c3e907225121-3.12.0a4+-5dcae3f | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.45 ms                                                                | 3.40 ms: 1.01x faster                                                      |
| regex_v8       | 22.0 ms                                                                | 21.7 ms: 1.01x faster                                                      |
| regex_dna      | 207 ms                                                                 | 210 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230202-linux-x86_64-python-5dcae3f0c3e907225121-3.12.0a4+-5dcae3f | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 24.5 us                                                                | 23.9 us: 1.02x faster                                                      |
| unpickle             | 13.2 us                                                                | 13.1 us: 1.01x faster                                                      |
| xml_etree_process    | 53.9 ms                                                                | 53.1 ms: 1.01x faster                                                      |
| xml_etree_generate   | 77.5 ms                                                                | 76.7 ms: 1.01x faster                                                      |
| unpickle_pure_python | 196 us                                                                 | 198 us: 1.01x slower                                                       |
| pickle_pure_python   | 282 us                                                                 | 285 us: 1.01x slower                                                       |
| pickle               | 10.2 us                                                                | 10.3 us: 1.01x slower                                                      |
| xml_etree_parse      | 147 ms                                                                 | 149 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (5): xml_etree_iterparse, pickle_dict, pickle_list, json_dumps, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230202-linux-x86_64-python-5dcae3f0c3e907225121-3.12.0a4+-5dcae3f | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.47 ms                                                                | 6.25 ms: 1.04x faster                                                      |
| python_startup         | 8.94 ms                                                                | 8.72 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230202-linux-x86_64-python-5dcae3f0c3e907225121-3.12.0a4+-5dcae3f | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.77 ms                                                                | 9.53 ms: 1.03x faster                                                      |
| django_template | 32.7 ms                                                                | 32.9 ms: 1.01x slower                                                      |
| genshi_xml      | 46.6 ms                                                                | 47.8 ms: 1.03x slower                                                      |
| genshi_text     | 20.4 ms                                                                | 21.3 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark              | bm-20230202-linux-x86_64-python-5dcae3f0c3e907225121-3.12.0a4+-5dcae3f | bm-20230202-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-fa5965d |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nqueens                | 79.0 ms                                                                | 75.8 ms: 1.04x faster                                                      |
| python_startup_no_site | 6.47 ms                                                                | 6.25 ms: 1.04x faster                                                      |
| mako                   | 9.77 ms                                                                | 9.53 ms: 1.03x faster                                                      |
| python_startup         | 8.94 ms                                                                | 8.72 ms: 1.02x faster                                                      |
| raytrace               | 288 ms                                                                 | 282 ms: 1.02x faster                                                       |
| json_loads             | 24.5 us                                                                | 23.9 us: 1.02x faster                                                      |
| thrift                 | 759 us                                                                 | 743 us: 1.02x faster                                                       |
| chaos                  | 65.8 ms                                                                | 64.5 ms: 1.02x faster                                                      |
| sqlglot_transpile      | 1.72 ms                                                                | 1.69 ms: 1.02x faster                                                      |
| sqlglot_normalize      | 106 ms                                                                 | 105 ms: 1.02x faster                                                       |
| scimark_monte_carlo    | 66.2 ms                                                                | 65.2 ms: 1.02x faster                                                      |
| sqlglot_parse          | 1.43 ms                                                                | 1.40 ms: 1.02x faster                                                      |
| pyflate                | 400 ms                                                                 | 394 ms: 1.02x faster                                                       |
| regex_effbot           | 3.45 ms                                                                | 3.40 ms: 1.01x faster                                                      |
| regex_v8               | 22.0 ms                                                                | 21.7 ms: 1.01x faster                                                      |
| fannkuch               | 366 ms                                                                 | 361 ms: 1.01x faster                                                       |
| unpickle               | 13.2 us                                                                | 13.1 us: 1.01x faster                                                      |
| xml_etree_process      | 53.9 ms                                                                | 53.1 ms: 1.01x faster                                                      |
| bench_thread_pool      | 787 us                                                                 | 777 us: 1.01x faster                                                       |
| hexiom                 | 6.00 ms                                                                | 5.93 ms: 1.01x faster                                                      |
| chameleon              | 6.34 ms                                                                | 6.26 ms: 1.01x faster                                                      |
| xml_etree_generate     | 77.5 ms                                                                | 76.7 ms: 1.01x faster                                                      |
| deepcopy_memo          | 34.4 us                                                                | 34.0 us: 1.01x faster                                                      |
| create_gc_cycles       | 1.48 ms                                                                | 1.46 ms: 1.01x faster                                                      |
| deepcopy_reduce        | 2.94 us                                                                | 2.91 us: 1.01x faster                                                      |
| telco                  | 6.38 ms                                                                | 6.33 ms: 1.01x faster                                                      |
| go                     | 135 ms                                                                 | 134 ms: 1.01x faster                                                       |
| sqlglot_optimize       | 51.3 ms                                                                | 50.9 ms: 1.01x faster                                                      |
| mdp                    | 2.57 sec                                                               | 2.56 sec: 1.01x faster                                                     |
| generators             | 78.6 ms                                                                | 78.1 ms: 1.01x faster                                                      |
| 2to3                   | 252 ms                                                                 | 251 ms: 1.01x faster                                                       |
| float                  | 72.2 ms                                                                | 71.9 ms: 1.00x faster                                                      |
| asyncio_tcp            | 498 ms                                                                 | 496 ms: 1.00x faster                                                       |
| sympy_integrate        | 19.7 ms                                                                | 19.8 ms: 1.00x slower                                                      |
| aiohttp                | 997 us                                                                 | 1.00 ms: 1.00x slower                                                      |
| dulwich_log            | 63.0 ms                                                                | 63.3 ms: 1.00x slower                                                      |
| sympy_str              | 269 ms                                                                 | 271 ms: 1.00x slower                                                       |
| deltablue              | 3.19 ms                                                                | 3.21 ms: 1.01x slower                                                      |
| django_template        | 32.7 ms                                                                | 32.9 ms: 1.01x slower                                                      |
| async_generators       | 352 ms                                                                 | 354 ms: 1.01x slower                                                       |
| sympy_expand           | 451 ms                                                                 | 455 ms: 1.01x slower                                                       |
| unpickle_pure_python   | 196 us                                                                 | 198 us: 1.01x slower                                                       |
| crypto_pyaes           | 72.5 ms                                                                | 73.1 ms: 1.01x slower                                                      |
| pickle_pure_python     | 282 us                                                                 | 285 us: 1.01x slower                                                       |
| async_tree_io          | 1.32 sec                                                               | 1.33 sec: 1.01x slower                                                     |
| pickle                 | 10.2 us                                                                | 10.3 us: 1.01x slower                                                      |
| xml_etree_parse        | 147 ms                                                                 | 149 ms: 1.01x slower                                                       |
| scimark_sor            | 105 ms                                                                 | 106 ms: 1.01x slower                                                       |
| scimark_lu             | 103 ms                                                                 | 105 ms: 1.01x slower                                                       |
| pprint_safe_repr       | 667 ms                                                                 | 676 ms: 1.01x slower                                                       |
| logging_silent         | 90.7 ns                                                                | 92.0 ns: 1.01x slower                                                      |
| coroutines             | 25.1 ms                                                                | 25.5 ms: 1.02x slower                                                      |
| regex_dna              | 207 ms                                                                 | 210 ms: 1.02x slower                                                       |
| richards               | 41.5 ms                                                                | 42.2 ms: 1.02x slower                                                      |
| pprint_pformat         | 1.37 sec                                                               | 1.39 sec: 1.02x slower                                                     |
| unpack_sequence        | 42.6 ns                                                                | 43.5 ns: 1.02x slower                                                      |
| genshi_xml             | 46.6 ms                                                                | 47.8 ms: 1.03x slower                                                      |
| pycparser              | 1.10 sec                                                               | 1.14 sec: 1.04x slower                                                     |
| gc_traversal           | 3.91 ms                                                                | 4.06 ms: 1.04x slower                                                      |
| coverage               | 95.6 ms                                                                | 99.5 ms: 1.04x slower                                                      |
| pidigits               | 189 ms                                                                 | 198 ms: 1.04x slower                                                       |
| genshi_text            | 20.4 ms                                                                | 21.3 ms: 1.04x slower                                                      |
| nbody                  | 94.5 ms                                                                | 98.9 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (28): scimark_fft, json, mypy, djangocms, scimark_sparse_mat_mult, regex_compile, sympy_sum, dask, spectral_norm, logging_format, xml_etree_iterparse, pickle_dict, bench_mp_pool, docutils, tornado_http, pickle_list, json_dumps, async_tree_none, unpickle_list, html5lib, gunicorn, logging_simple, deepcopy, async_tree_cpu_io_mixed, pathlib, sqlite_synth, meteor_contest, async_tree_memoization
