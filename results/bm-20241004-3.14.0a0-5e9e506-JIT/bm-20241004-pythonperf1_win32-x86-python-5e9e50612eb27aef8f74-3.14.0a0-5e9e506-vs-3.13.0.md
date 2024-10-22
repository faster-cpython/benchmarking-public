# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-x86
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.07x faster
- HPT reliability: 92.24%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 261 ms: 1.03x slower                                                           |
| docutils       | 1.82 sec                                                        | 2.04 sec: 1.12x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.9 ms: 1.03x faster                                                          |
| tornado_http   | 104 ms                                                          | 109 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.13x faster                                                           |
| async_tree_none           | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| asyncio_tcp               | 842 ms                                                          | 771 ms: 1.09x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 279 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 468 ms: 1.06x faster                                                           |
| async_tree_io             | 537 ms                                                          | 524 ms: 1.02x faster                                                           |
| coroutines                | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| async_generators          | 274 ms                                                          | 326 ms: 1.19x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 50.4 ms: 1.62x faster                                                          |
| float          | 57.8 ms                                                         | 46.2 ms: 1.25x faster                                                          |
| pidigits       | 202 ms                                                          | 199 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 15.3 ms: 1.02x faster                                                          |
| regex_compile  | 103 ms                                                          | 105 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 54.7 ms: 1.14x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 41.5 ms: 1.08x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 6.98 ms: 1.06x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 2.93 us: 1.06x faster                                                          |
| unpickle_pure_python | 162 us                                                          | 158 us: 1.02x faster                                                           |
| pickle_dict          | 21.7 us                                                         | 21.3 us: 1.02x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.4 us: 1.02x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 64.5 ms: 1.01x faster                                                          |
| pickle               | 8.42 us                                                         | 8.37 us: 1.01x faster                                                          |
| pickle_pure_python   | 238 us                                                          | 242 us: 1.02x slower                                                           |
| pickle_list          | 3.40 us                                                         | 3.47 us: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                                          |
| python_startup         | 24.3 ms                                                         | 26.8 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.57 ms: 1.31x faster                                                          |
| django_template | 32.7 ms                                                         | 32.0 ms: 1.02x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 23.8 ms: 1.06x slower                                                          |
| genshi_xml      | 49.5 ms                                                         | 56.2 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 774 us: 13.11x faster                                                          |
| coverage                  | 333 ms                                                          | 53.5 ms: 6.23x faster                                                          |
| sqlglot_normalize         | 220 ms                                                          | 102 ms: 2.15x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 16.0 us: 1.64x faster                                                          |
| nbody                     | 81.9 ms                                                         | 50.4 ms: 1.62x faster                                                          |
| scimark_sor               | 91.8 ms                                                         | 68.5 ms: 1.34x faster                                                          |
| mako                      | 7.31 ms                                                         | 5.57 ms: 1.31x faster                                                          |
| deepcopy                  | 307 us                                                          | 234 us: 1.31x faster                                                           |
| scimark_monte_carlo       | 50.3 ms                                                         | 39.0 ms: 1.29x faster                                                          |
| float                     | 57.8 ms                                                         | 46.2 ms: 1.25x faster                                                          |
| spectral_norm             | 71.3 ms                                                         | 58.4 ms: 1.22x faster                                                          |
| fannkuch                  | 293 ms                                                          | 245 ms: 1.20x faster                                                           |
| deepcopy_reduce           | 2.85 us                                                         | 2.43 us: 1.17x faster                                                          |
| scimark_fft               | 206 ms                                                          | 177 ms: 1.17x faster                                                           |
| go                        | 111 ms                                                          | 97.1 ms: 1.15x faster                                                          |
| tomli_loads               | 1.73 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| xml_etree_generate        | 62.6 ms                                                         | 54.7 ms: 1.14x faster                                                          |
| pprint_safe_repr          | 644 ms                                                          | 565 ms: 1.14x faster                                                           |
| crypto_pyaes              | 58.2 ms                                                         | 51.2 ms: 1.14x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.13x faster                                                           |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.60 ms: 1.12x faster                                                          |
| async_tree_none           | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| pprint_pformat            | 1.30 sec                                                        | 1.18 sec: 1.10x faster                                                         |
| asyncio_tcp               | 842 ms                                                          | 771 ms: 1.09x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| xml_etree_process         | 45.0 ms                                                         | 41.5 ms: 1.08x faster                                                          |
| async_tree_memoization    | 302 ms                                                          | 279 ms: 1.08x faster                                                           |
| scimark_lu                | 63.5 ms                                                         | 59.1 ms: 1.07x faster                                                          |
| json_dumps                | 7.40 ms                                                         | 6.98 ms: 1.06x faster                                                          |
| unpack_sequence           | 42.9 ns                                                         | 40.5 ns: 1.06x faster                                                          |
| pycparser                 | 869 ms                                                          | 822 ms: 1.06x faster                                                           |
| unpickle_list             | 3.09 us                                                         | 2.93 us: 1.06x faster                                                          |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 468 ms: 1.06x faster                                                           |
| logging_silent            | 61.6 ns                                                         | 58.6 ns: 1.05x faster                                                          |
| sqlite_synth              | 1.97 us                                                         | 1.89 us: 1.04x faster                                                          |
| telco                     | 6.67 ms                                                         | 6.42 ms: 1.04x faster                                                          |
| comprehensions            | 12.7 us                                                         | 12.3 us: 1.04x faster                                                          |
| html5lib                  | 48.3 ms                                                         | 46.9 ms: 1.03x faster                                                          |
| meteor_contest            | 77.0 ms                                                         | 75.0 ms: 1.03x faster                                                          |
| async_tree_io             | 537 ms                                                          | 524 ms: 1.02x faster                                                           |
| regex_v8                  | 15.6 ms                                                         | 15.3 ms: 1.02x faster                                                          |
| django_template           | 32.7 ms                                                         | 32.0 ms: 1.02x faster                                                          |
| unpickle_pure_python      | 162 us                                                          | 158 us: 1.02x faster                                                           |
| pickle_dict               | 21.7 us                                                         | 21.3 us: 1.02x faster                                                          |
| pathlib                   | 89.4 ms                                                         | 87.8 ms: 1.02x faster                                                          |
| unpickle                  | 10.5 us                                                         | 10.4 us: 1.02x faster                                                          |
| pidigits                  | 202 ms                                                          | 199 ms: 1.02x faster                                                           |
| nqueens                   | 75.1 ms                                                         | 73.9 ms: 1.02x faster                                                          |
| xml_etree_iterparse       | 65.1 ms                                                         | 64.5 ms: 1.01x faster                                                          |
| logging_format            | 8.57 us                                                         | 8.52 us: 1.01x faster                                                          |
| pickle                    | 8.42 us                                                         | 8.37 us: 1.01x faster                                                          |
| regex_compile             | 103 ms                                                          | 105 ms: 1.01x slower                                                           |
| sqlglot_parse             | 1.05 ms                                                         | 1.07 ms: 1.02x slower                                                          |
| mdp                       | 1.67 sec                                                        | 1.70 sec: 1.02x slower                                                         |
| pickle_pure_python        | 238 us                                                          | 242 us: 1.02x slower                                                           |
| logging_simple            | 7.87 us                                                         | 8.02 us: 1.02x slower                                                          |
| pickle_list               | 3.40 us                                                         | 3.47 us: 1.02x slower                                                          |
| typing_runtime_protocols  | 136 us                                                          | 139 us: 1.02x slower                                                           |
| chaos                     | 51.2 ms                                                         | 52.4 ms: 1.02x slower                                                          |
| python_startup_no_site    | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                                          |
| 2to3                      | 253 ms                                                          | 261 ms: 1.03x slower                                                           |
| tornado_http              | 104 ms                                                          | 109 ms: 1.05x slower                                                           |
| sympy_expand              | 375 ms                                                          | 394 ms: 1.05x slower                                                           |
| sympy_str                 | 215 ms                                                          | 227 ms: 1.05x slower                                                           |
| sqlglot_transpile         | 1.29 ms                                                         | 1.37 ms: 1.06x slower                                                          |
| genshi_text               | 22.4 ms                                                         | 23.8 ms: 1.06x slower                                                          |
| sympy_sum                 | 108 ms                                                          | 117 ms: 1.09x slower                                                           |
| deltablue                 | 2.41 ms                                                         | 2.63 ms: 1.09x slower                                                          |
| python_startup            | 24.3 ms                                                         | 26.8 ms: 1.10x slower                                                          |
| coroutines                | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| docutils                  | 1.82 sec                                                        | 2.04 sec: 1.12x slower                                                         |
| sympy_integrate           | 15.2 ms                                                         | 17.1 ms: 1.13x slower                                                          |
| genshi_xml                | 49.5 ms                                                         | 56.2 ms: 1.14x slower                                                          |
| sqlglot_optimize          | 42.5 ms                                                         | 49.7 ms: 1.17x slower                                                          |
| hexiom                    | 4.64 ms                                                         | 5.48 ms: 1.18x slower                                                          |
| richards                  | 33.8 ms                                                         | 39.9 ms: 1.18x slower                                                          |
| richards_super            | 38.0 ms                                                         | 45.2 ms: 1.19x slower                                                          |
| async_generators          | 274 ms                                                          | 326 ms: 1.19x slower                                                           |
| gc_traversal              | 1.45 ms                                                         | 1.78 ms: 1.23x slower                                                          |
| generators                | 22.1 ms                                                         | 27.1 ms: 1.23x slower                                                          |
| raytrace                  | 205 ms                                                          | 255 ms: 1.24x slower                                                           |
| pylint                    | 225 ms                                                          | 282 ms: 1.25x slower                                                           |
| bench_mp_pool             | 74.3 ms                                                         | 94.3 ms: 1.27x slower                                                          |
| create_gc_cycles          | 713 us                                                          | 1.16 ms: 1.63x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                                   |

Benchmark hidden because not significant (11): json, regex_dna, pyflate, asyncio_tcp_ssl, json_loads, regex_effbot, dulwich_log, bench_thread_pool, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_io_tg
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

# HPT report

- Reliability score: 92.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown