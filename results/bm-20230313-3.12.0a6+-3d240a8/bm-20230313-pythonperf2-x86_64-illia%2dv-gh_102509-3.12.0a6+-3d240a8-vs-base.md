
# Results vs. base

- fork: illia-v
- ref: gh_102509
- machine: linux-x86_64
- commit hash: 3d240a8
- commit date: 2023-03-13
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230313-pythonperf2-x86_64-python-71e37d907905b0504c5b-3.12.0a6+-71e37d9 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 2.82 sec                                                                     | 2.81 sec: 1.00x faster                                               |
| html5lib       | 66.6 ms                                                                      | 68.5 ms: 1.03x slower                                                |
| tornado_http   | 115 ms                                                                       | 117 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                         |

Benchmark hidden because not significant (2): 2to3, chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230313-pythonperf2-x86_64-python-71e37d907905b0504c5b-3.12.0a6+-71e37d9 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 73.5 ms                                                                      | 72.3 ms: 1.02x faster                                                |
| nbody          | 84.6 ms                                                                      | 83.3 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230313-pythonperf2-x86_64-python-71e37d907905b0504c5b-3.12.0a6+-71e37d9 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 147 ms                                                                       | 149 ms: 1.01x slower                                                 |
| regex_dna      | 236 ms                                                                       | 239 ms: 1.02x slower                                                 |
| regex_effbot   | 3.43 ms                                                                      | 3.53 ms: 1.03x slower                                                |
| regex_v8       | 23.3 ms                                                                      | 24.1 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230313-pythonperf2-x86_64-python-71e37d907905b0504c5b-3.12.0a6+-71e37d9 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle             | 13.6 us                                                                      | 13.2 us: 1.03x faster                                                |
| tomli_loads          | 2.16 sec                                                                     | 2.11 sec: 1.03x faster                                               |
| pickle               | 10.2 us                                                                      | 10.2 us: 1.00x faster                                                |
| json_loads           | 23.9 us                                                                      | 24.2 us: 1.01x slower                                                |
| pickle_pure_python   | 303 us                                                                       | 307 us: 1.01x slower                                                 |
| xml_etree_generate   | 83.8 ms                                                                      | 85.1 ms: 1.02x slower                                                |
| xml_etree_process    | 56.9 ms                                                                      | 57.8 ms: 1.02x slower                                                |
| xml_etree_iterparse  | 102 ms                                                                       | 104 ms: 1.02x slower                                                 |
| json_dumps           | 10.2 ms                                                                      | 10.4 ms: 1.02x slower                                                |
| unpickle_pure_python | 200 us                                                                       | 206 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                                        | 1.00x slower                                                         |

Benchmark hidden because not significant (4): pickle_dict, xml_etree_parse, pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230313-pythonperf2-x86_64-python-71e37d907905b0504c5b-3.12.0a6+-71e37d9 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 57.0 ms                                                                      | 55.1 ms: 1.03x faster                                                |
| django_template | 40.3 ms                                                                      | 39.6 ms: 1.02x faster                                                |
| mako            | 9.88 ms                                                                      | 9.99 ms: 1.01x slower                                                |
| genshi_text     | 25.2 ms                                                                      | 26.2 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                                        | 1.00x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20230313-pythonperf2-x86_64-python-71e37d907905b0504c5b-3.12.0a6+-71e37d9 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|--------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| fannkuch                 | 447 ms                                                                       | 409 ms: 1.09x faster                                                 |
| gc_traversal             | 4.18 ms                                                                      | 3.96 ms: 1.06x faster                                                |
| logging_simple           | 7.12 us                                                                      | 6.80 us: 1.05x faster                                                |
| pathlib                  | 19.0 ms                                                                      | 18.4 ms: 1.03x faster                                                |
| genshi_xml               | 57.0 ms                                                                      | 55.1 ms: 1.03x faster                                                |
| sqlglot_parse            | 1.62 ms                                                                      | 1.57 ms: 1.03x faster                                                |
| unpickle                 | 13.6 us                                                                      | 13.2 us: 1.03x faster                                                |
| hexiom                   | 6.55 ms                                                                      | 6.36 ms: 1.03x faster                                                |
| spectral_norm            | 92.1 ms                                                                      | 89.5 ms: 1.03x faster                                                |
| tomli_loads              | 2.16 sec                                                                     | 2.11 sec: 1.03x faster                                               |
| sqlglot_transpile        | 1.98 ms                                                                      | 1.93 ms: 1.03x faster                                                |
| scimark_fft              | 267 ms                                                                       | 261 ms: 1.02x faster                                                 |
| pyflate                  | 434 ms                                                                       | 424 ms: 1.02x faster                                                 |
| scimark_monte_carlo      | 67.8 ms                                                                      | 66.4 ms: 1.02x faster                                                |
| coroutines               | 25.8 ms                                                                      | 25.3 ms: 1.02x faster                                                |
| coverage                 | 81.6 ms                                                                      | 80.1 ms: 1.02x faster                                                |
| float                    | 73.5 ms                                                                      | 72.3 ms: 1.02x faster                                                |
| django_template          | 40.3 ms                                                                      | 39.6 ms: 1.02x faster                                                |
| nbody                    | 84.6 ms                                                                      | 83.3 ms: 1.02x faster                                                |
| go                       | 162 ms                                                                       | 159 ms: 1.01x faster                                                 |
| typing_runtime_protocols | 519 us                                                                       | 513 us: 1.01x faster                                                 |
| pprint_pformat           | 1.57 sec                                                                     | 1.56 sec: 1.01x faster                                               |
| deepcopy_reduce          | 3.37 us                                                                      | 3.34 us: 1.01x faster                                                |
| raytrace                 | 290 ms                                                                       | 288 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult  | 3.82 ms                                                                      | 3.79 ms: 1.01x faster                                                |
| telco                    | 6.96 ms                                                                      | 6.92 ms: 1.01x faster                                                |
| pprint_safe_repr         | 772 ms                                                                       | 768 ms: 1.01x faster                                                 |
| docutils                 | 2.82 sec                                                                     | 2.81 sec: 1.00x faster                                               |
| pickle                   | 10.2 us                                                                      | 10.2 us: 1.00x faster                                                |
| sqlite_synth             | 2.60 us                                                                      | 2.59 us: 1.00x faster                                                |
| sqlglot_optimize         | 58.5 ms                                                                      | 58.4 ms: 1.00x faster                                                |
| crypto_pyaes             | 82.4 ms                                                                      | 82.8 ms: 1.01x slower                                                |
| asyncio_tcp              | 384 ms                                                                       | 386 ms: 1.01x slower                                                 |
| sympy_str                | 332 ms                                                                       | 334 ms: 1.01x slower                                                 |
| sqlglot_normalize        | 119 ms                                                                       | 120 ms: 1.01x slower                                                 |
| scimark_lu               | 99.5 ms                                                                      | 100 ms: 1.01x slower                                                 |
| sympy_expand             | 536 ms                                                                       | 540 ms: 1.01x slower                                                 |
| sympy_integrate          | 25.1 ms                                                                      | 25.3 ms: 1.01x slower                                                |
| json                     | 5.02 ms                                                                      | 5.07 ms: 1.01x slower                                                |
| json_loads               | 23.9 us                                                                      | 24.2 us: 1.01x slower                                                |
| mako                     | 9.88 ms                                                                      | 9.99 ms: 1.01x slower                                                |
| regex_compile            | 147 ms                                                                       | 149 ms: 1.01x slower                                                 |
| async_generators         | 377 ms                                                                       | 382 ms: 1.01x slower                                                 |
| sympy_sum                | 185 ms                                                                       | 187 ms: 1.01x slower                                                 |
| richards                 | 44.8 ms                                                                      | 45.3 ms: 1.01x slower                                                |
| meteor_contest           | 127 ms                                                                       | 129 ms: 1.01x slower                                                 |
| pickle_pure_python       | 303 us                                                                       | 307 us: 1.01x slower                                                 |
| xml_etree_generate       | 83.8 ms                                                                      | 85.1 ms: 1.02x slower                                                |
| regex_dna                | 236 ms                                                                       | 239 ms: 1.02x slower                                                 |
| tornado_http             | 115 ms                                                                       | 117 ms: 1.02x slower                                                 |
| xml_etree_process        | 56.9 ms                                                                      | 57.8 ms: 1.02x slower                                                |
| pycparser                | 1.24 sec                                                                     | 1.26 sec: 1.02x slower                                               |
| xml_etree_iterparse      | 102 ms                                                                       | 104 ms: 1.02x slower                                                 |
| json_dumps               | 10.2 ms                                                                      | 10.4 ms: 1.02x slower                                                |
| unpack_sequence          | 44.1 ns                                                                      | 45.0 ns: 1.02x slower                                                |
| mdp                      | 2.57 sec                                                                     | 2.62 sec: 1.02x slower                                               |
| nqueens                  | 97.7 ms                                                                      | 99.9 ms: 1.02x slower                                                |
| deepcopy                 | 379 us                                                                       | 387 us: 1.02x slower                                                 |
| deepcopy_memo            | 35.2 us                                                                      | 36.0 us: 1.02x slower                                                |
| regex_effbot             | 3.43 ms                                                                      | 3.53 ms: 1.03x slower                                                |
| html5lib                 | 66.6 ms                                                                      | 68.5 ms: 1.03x slower                                                |
| unpickle_pure_python     | 200 us                                                                       | 206 us: 1.03x slower                                                 |
| genshi_text              | 25.2 ms                                                                      | 26.2 ms: 1.04x slower                                                |
| thrift                   | 925 us                                                                       | 960 us: 1.04x slower                                                 |
| regex_v8                 | 23.3 ms                                                                      | 24.1 ms: 1.04x slower                                                |
| richards_super           | 57.2 ms                                                                      | 59.5 ms: 1.04x slower                                                |
| logging_silent           | 95.2 ns                                                                      | 99.6 ns: 1.05x slower                                                |
| chaos                    | 72.7 ms                                                                      | 76.1 ms: 1.05x slower                                                |
| scimark_sor              | 104 ms                                                                       | 110 ms: 1.05x slower                                                 |
| Geometric mean           | (ref)                                                                        | 1.00x slower                                                         |

Benchmark hidden because not significant (23): logging_format, pickle_dict, create_gc_cycles, async_tree_cpu_io_mixed, xml_etree_parse, pickle_list, deltablue, 2to3, python_startup, asyncio_tcp_ssl, python_startup_no_site, pidigits, chameleon, comprehensions, async_tree_none, async_tree_io, dulwich_log, async_tree_memoization, unpickle_list, generators, dask, bench_thread_pool, bench_mp_pool
