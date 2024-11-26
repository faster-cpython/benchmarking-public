# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.086x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                 | 301 ms: 1.08x slower                                                      |
| docutils       | 2.91 sec                                                               | 3.01 sec: 1.03x slower                                                    |
| html5lib       | 65.2 ms                                                                | 68.6 ms: 1.05x slower                                                     |
| sphinx         | 1.17 sec                                                               | 1.21 sec: 1.04x slower                                                    |
| tornado_http   | 94.6 ms                                                                | 96.7 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg          | 977 ms                                                                 | 985 ms: 1.01x slower                                                      |
| async_generators          | 460 ms                                                                 | 464 ms: 1.01x slower                                                      |
| coroutines                | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed   | 577 ms                                                                 | 589 ms: 1.02x slower                                                      |
| async_tree_memoization_tg | 380 ms                                                                 | 389 ms: 1.03x slower                                                      |
| async_tree_io             | 855 ms                                                                 | 880 ms: 1.03x slower                                                      |
| async_tree_memoization    | 416 ms                                                                 | 433 ms: 1.04x slower                                                      |
| async_tree_none           | 336 ms                                                                 | 352 ms: 1.04x slower                                                      |
| Geometric mean            | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 188 ms: 1.00x slower                                                      |
| float          | 76.1 ms                                                                | 83.5 ms: 1.10x slower                                                     |
| nbody          | 81.7 ms                                                                | 102 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.11x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.65 ms: 1.03x faster                                                     |
| regex_dna      | 217 ms                                                                 | 213 ms: 1.02x faster                                                      |
| regex_v8       | 24.7 ms                                                                | 25.9 ms: 1.05x slower                                                     |
| regex_compile  | 139 ms                                                                 | 154 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 26.6 us                                                                | 27.0 us: 1.01x slower                                                     |
| xml_etree_parse      | 149 ms                                                                 | 152 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 100 ms                                                                 | 105 ms: 1.05x slower                                                      |
| json_dumps           | 11.0 ms                                                                | 11.7 ms: 1.06x slower                                                     |
| pickle_pure_python   | 316 us                                                                 | 349 us: 1.11x slower                                                      |
| tomli_loads          | 1.92 sec                                                               | 2.18 sec: 1.14x slower                                                    |
| unpickle_pure_python | 216 us                                                                 | 248 us: 1.15x slower                                                      |
| xml_etree_generate   | 78.4 ms                                                                | 90.4 ms: 1.15x slower                                                     |
| xml_etree_process    | 55.3 ms                                                                | 63.7 ms: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.09x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.08 ms: 1.00x slower                                                     |
| python_startup         | 11.8 ms                                                                | 11.8 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 61.8 ms                                                                | 64.5 ms: 1.04x slower                                                     |
| genshi_text     | 26.3 ms                                                                | 27.6 ms: 1.05x slower                                                     |
| django_template | 37.1 ms                                                                | 39.2 ms: 1.06x slower                                                     |
| mako            | 9.87 ms                                                                | 12.1 ms: 1.23x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.09x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|---------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot              | 3.77 ms                                                                | 3.65 ms: 1.03x faster                                                     |
| regex_dna                 | 217 ms                                                                 | 213 ms: 1.02x faster                                                      |
| pidigits                  | 187 ms                                                                 | 188 ms: 1.00x slower                                                      |
| python_startup_no_site    | 7.05 ms                                                                | 7.08 ms: 1.00x slower                                                     |
| python_startup            | 11.8 ms                                                                | 11.8 ms: 1.00x slower                                                     |
| create_gc_cycles          | 2.67 ms                                                                | 2.69 ms: 1.01x slower                                                     |
| async_tree_io_tg          | 977 ms                                                                 | 985 ms: 1.01x slower                                                      |
| logging_format            | 6.22 us                                                                | 6.27 us: 1.01x slower                                                     |
| async_generators          | 460 ms                                                                 | 464 ms: 1.01x slower                                                      |
| pathlib                   | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                                     |
| bench_mp_pool             | 83.7 ms                                                                | 84.6 ms: 1.01x slower                                                     |
| coroutines                | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                     |
| json_loads                | 26.6 us                                                                | 27.0 us: 1.01x slower                                                     |
| thrift                    | 789 us                                                                 | 801 us: 1.01x slower                                                      |
| sqlalchemy_imperative     | 17.8 ms                                                                | 18.1 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed   | 577 ms                                                                 | 589 ms: 1.02x slower                                                      |
| tornado_http              | 94.6 ms                                                                | 96.7 ms: 1.02x slower                                                     |
| sqlalchemy_declarative    | 147 ms                                                                 | 151 ms: 1.02x slower                                                      |
| xml_etree_parse           | 149 ms                                                                 | 152 ms: 1.03x slower                                                      |
| async_tree_memoization_tg | 380 ms                                                                 | 389 ms: 1.03x slower                                                      |
| logging_simple            | 5.61 us                                                                | 5.77 us: 1.03x slower                                                     |
| async_tree_io             | 855 ms                                                                 | 880 ms: 1.03x slower                                                      |
| gc_traversal              | 4.55 ms                                                                | 4.70 ms: 1.03x slower                                                     |
| docutils                  | 2.91 sec                                                               | 3.01 sec: 1.03x slower                                                    |
| json                      | 4.98 ms                                                                | 5.15 ms: 1.03x slower                                                     |
| pylint                    | 325 ms                                                                 | 337 ms: 1.03x slower                                                      |
| mdp                       | 2.57 sec                                                               | 2.66 sec: 1.04x slower                                                    |
| dulwich_log               | 66.4 ms                                                                | 68.9 ms: 1.04x slower                                                     |
| sphinx                    | 1.17 sec                                                               | 1.21 sec: 1.04x slower                                                    |
| sympy_sum                 | 177 ms                                                                 | 184 ms: 1.04x slower                                                      |
| async_tree_memoization    | 416 ms                                                                 | 433 ms: 1.04x slower                                                      |
| sympy_expand              | 503 ms                                                                 | 525 ms: 1.04x slower                                                      |
| genshi_xml                | 61.8 ms                                                                | 64.5 ms: 1.04x slower                                                     |
| async_tree_none           | 336 ms                                                                 | 352 ms: 1.04x slower                                                      |
| xml_etree_iterparse       | 100 ms                                                                 | 105 ms: 1.05x slower                                                      |
| sympy_str                 | 306 ms                                                                 | 321 ms: 1.05x slower                                                      |
| genshi_text               | 26.3 ms                                                                | 27.6 ms: 1.05x slower                                                     |
| bench_thread_pool         | 877 us                                                                 | 921 us: 1.05x slower                                                      |
| regex_v8                  | 24.7 ms                                                                | 25.9 ms: 1.05x slower                                                     |
| html5lib                  | 65.2 ms                                                                | 68.6 ms: 1.05x slower                                                     |
| django_template           | 37.1 ms                                                                | 39.2 ms: 1.06x slower                                                     |
| json_dumps                | 11.0 ms                                                                | 11.7 ms: 1.06x slower                                                     |
| scimark_lu                | 115 ms                                                                 | 123 ms: 1.06x slower                                                      |
| sympy_integrate           | 23.6 ms                                                                | 25.2 ms: 1.07x slower                                                     |
| sqlglot_transpile         | 1.71 ms                                                                | 1.84 ms: 1.08x slower                                                     |
| 2to3                      | 279 ms                                                                 | 301 ms: 1.08x slower                                                      |
| sqlglot_normalize         | 115 ms                                                                 | 125 ms: 1.08x slower                                                      |
| typing_runtime_protocols  | 169 us                                                                 | 183 us: 1.09x slower                                                      |
| sqlglot_optimize          | 60.1 ms                                                                | 65.7 ms: 1.09x slower                                                     |
| float                     | 76.1 ms                                                                | 83.5 ms: 1.10x slower                                                     |
| sqlglot_parse             | 1.34 ms                                                                | 1.47 ms: 1.10x slower                                                     |
| deepcopy_reduce           | 2.77 us                                                                | 3.07 us: 1.11x slower                                                     |
| pickle_pure_python        | 316 us                                                                 | 349 us: 1.11x slower                                                      |
| regex_compile             | 139 ms                                                                 | 154 ms: 1.11x slower                                                      |
| telco                     | 7.59 ms                                                                | 8.42 ms: 1.11x slower                                                     |
| pycparser                 | 1.15 sec                                                               | 1.29 sec: 1.12x slower                                                    |
| logging_silent            | 109 ns                                                                 | 122 ns: 1.12x slower                                                      |
| meteor_contest            | 108 ms                                                                 | 122 ms: 1.13x slower                                                      |
| tomli_loads               | 1.92 sec                                                               | 2.18 sec: 1.14x slower                                                    |
| scimark_sparse_mat_mult   | 4.60 ms                                                                | 5.23 ms: 1.14x slower                                                     |
| deepcopy                  | 269 us                                                                 | 309 us: 1.15x slower                                                      |
| unpickle_pure_python      | 216 us                                                                 | 248 us: 1.15x slower                                                      |
| xml_etree_generate        | 78.4 ms                                                                | 90.4 ms: 1.15x slower                                                     |
| xml_etree_process         | 55.3 ms                                                                | 63.7 ms: 1.15x slower                                                     |
| raytrace                  | 283 ms                                                                 | 327 ms: 1.15x slower                                                      |
| spectral_norm             | 116 ms                                                                 | 135 ms: 1.16x slower                                                      |
| bpe_tokeniser             | 4.44 sec                                                               | 5.17 sec: 1.16x slower                                                    |
| generators                | 35.5 ms                                                                | 41.6 ms: 1.17x slower                                                     |
| scimark_fft               | 323 ms                                                                 | 382 ms: 1.18x slower                                                      |
| pyflate                   | 445 ms                                                                 | 531 ms: 1.19x slower                                                      |
| nqueens                   | 88.8 ms                                                                | 107 ms: 1.20x slower                                                      |
| deepcopy_memo             | 29.3 us                                                                | 35.3 us: 1.20x slower                                                     |
| pprint_safe_repr          | 722 ms                                                                 | 870 ms: 1.21x slower                                                      |
| deltablue                 | 3.23 ms                                                                | 3.93 ms: 1.21x slower                                                     |
| chaos                     | 59.7 ms                                                                | 72.9 ms: 1.22x slower                                                     |
| pprint_pformat            | 1.48 sec                                                               | 1.81 sec: 1.22x slower                                                    |
| mako                      | 9.87 ms                                                                | 12.1 ms: 1.23x slower                                                     |
| hexiom                    | 7.13 ms                                                                | 8.79 ms: 1.23x slower                                                     |
| go                        | 133 ms                                                                 | 165 ms: 1.24x slower                                                      |
| crypto_pyaes              | 68.3 ms                                                                | 84.6 ms: 1.24x slower                                                     |
| scimark_monte_carlo       | 64.5 ms                                                                | 80.7 ms: 1.25x slower                                                     |
| nbody                     | 81.7 ms                                                                | 102 ms: 1.25x slower                                                      |
| scimark_sor               | 119 ms                                                                 | 151 ms: 1.27x slower                                                      |
| comprehensions            | 17.0 us                                                                | 22.0 us: 1.29x slower                                                     |
| fannkuch                  | 376 ms                                                                 | 486 ms: 1.29x slower                                                      |
| richards_super            | 45.5 ms                                                                | 61.5 ms: 1.35x slower                                                     |
| richards                  | 41.8 ms                                                                | 59.1 ms: 1.42x slower                                                     |
| Geometric mean            | (ref)                                                                  | 1.09x slower                                                              |

Benchmark hidden because not significant (4): asyncio_websockets, coverage, async_tree_cpu_io_mixed_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.086x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.00x