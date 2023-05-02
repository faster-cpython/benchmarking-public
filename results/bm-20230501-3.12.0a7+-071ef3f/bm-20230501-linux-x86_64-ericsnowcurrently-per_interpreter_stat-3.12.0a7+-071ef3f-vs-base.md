
# Results vs. base

- fork: ericsnowcurrently
- ref: per_interpreter_stat
- machine: linux-x86_64
- commit hash: 071ef3f
- commit date: 2023-05-01
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 268 ms                                                                 | 271 ms: 1.01x slower                                                              |
| docutils       | 2.71 sec                                                               | 2.72 sec: 1.01x slower                                                            |
| tornado_http   | 98.5 ms                                                                | 102 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                 | 189 ms: 1.05x faster                                                              |
| nbody          | 89.2 ms                                                                | 87.4 ms: 1.02x faster                                                             |
| float          | 82.0 ms                                                                | 81.2 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.44 ms                                                                | 3.40 ms: 1.01x faster                                                             |
| regex_dna      | 210 ms                                                                 | 209 ms: 1.00x faster                                                              |
| regex_v8       | 22.1 ms                                                                | 22.4 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle             | 15.7 us                                                                | 14.4 us: 1.09x faster                                                             |
| unpickle_list        | 5.19 us                                                                | 4.95 us: 1.05x faster                                                             |
| pickle_list          | 4.79 us                                                                | 4.60 us: 1.04x faster                                                             |
| pickle_pure_python   | 319 us                                                                 | 316 us: 1.01x faster                                                              |
| pickle_dict          | 32.3 us                                                                | 32.4 us: 1.00x slower                                                             |
| json_dumps           | 10.1 ms                                                                | 10.1 ms: 1.01x slower                                                             |
| unpickle_pure_python | 217 us                                                                 | 218 us: 1.01x slower                                                              |
| xml_etree_parse      | 152 ms                                                                 | 153 ms: 1.01x slower                                                              |
| xml_etree_iterparse  | 103 ms                                                                 | 104 ms: 1.01x slower                                                              |
| xml_etree_generate   | 84.0 ms                                                                | 85.8 ms: 1.02x slower                                                             |
| xml_etree_process    | 58.2 ms                                                                | 60.4 ms: 1.04x slower                                                             |
| pickle               | 10.3 us                                                                | 10.8 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 9.06 ms                                                                | 9.15 ms: 1.01x slower                                                             |
| python_startup_no_site | 6.65 ms                                                                | 6.71 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text    | 22.7 ms                                                                | 22.3 ms: 1.02x faster                                                             |
| mako           | 10.8 ms                                                                | 10.7 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20230501-linux-x86_64-python-f73abf8e03fd370c86fb-3.12.0a7+-f73abf8 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle               | 15.7 us                                                                | 14.4 us: 1.09x faster                                                             |
| unpickle_list          | 5.19 us                                                                | 4.95 us: 1.05x faster                                                             |
| pidigits               | 198 ms                                                                 | 189 ms: 1.05x faster                                                              |
| scimark_sor            | 126 ms                                                                 | 121 ms: 1.04x faster                                                              |
| pickle_list            | 4.79 us                                                                | 4.60 us: 1.04x faster                                                             |
| coroutines             | 23.0 ms                                                                | 22.4 ms: 1.03x faster                                                             |
| nbody                  | 89.2 ms                                                                | 87.4 ms: 1.02x faster                                                             |
| logging_silent         | 101 ns                                                                 | 99.0 ns: 1.02x faster                                                             |
| deltablue              | 3.54 ms                                                                | 3.47 ms: 1.02x faster                                                             |
| scimark_lu             | 114 ms                                                                 | 112 ms: 1.02x faster                                                              |
| crypto_pyaes           | 79.5 ms                                                                | 77.9 ms: 1.02x faster                                                             |
| deepcopy_memo          | 39.0 us                                                                | 38.3 us: 1.02x faster                                                             |
| thrift                 | 811 us                                                                 | 797 us: 1.02x faster                                                              |
| genshi_text            | 22.7 ms                                                                | 22.3 ms: 1.02x faster                                                             |
| hexiom                 | 6.22 ms                                                                | 6.12 ms: 1.02x faster                                                             |
| raytrace               | 306 ms                                                                 | 302 ms: 1.02x faster                                                              |
| mako                   | 10.8 ms                                                                | 10.7 ms: 1.01x faster                                                             |
| sqlite_synth           | 2.70 us                                                                | 2.67 us: 1.01x faster                                                             |
| generators             | 31.0 ms                                                                | 30.7 ms: 1.01x faster                                                             |
| regex_effbot           | 3.44 ms                                                                | 3.40 ms: 1.01x faster                                                             |
| float                  | 82.0 ms                                                                | 81.2 ms: 1.01x faster                                                             |
| pickle_pure_python     | 319 us                                                                 | 316 us: 1.01x faster                                                              |
| scimark_monte_carlo    | 73.0 ms                                                                | 72.5 ms: 1.01x faster                                                             |
| go                     | 136 ms                                                                 | 136 ms: 1.00x faster                                                              |
| regex_dna              | 210 ms                                                                 | 209 ms: 1.00x faster                                                              |
| pickle_dict            | 32.3 us                                                                | 32.4 us: 1.00x slower                                                             |
| asyncio_tcp            | 511 ms                                                                 | 513 ms: 1.00x slower                                                              |
| json_dumps             | 10.1 ms                                                                | 10.1 ms: 1.01x slower                                                             |
| unpickle_pure_python   | 217 us                                                                 | 218 us: 1.01x slower                                                              |
| docutils               | 2.71 sec                                                               | 2.72 sec: 1.01x slower                                                            |
| pprint_safe_repr       | 733 ms                                                                 | 738 ms: 1.01x slower                                                              |
| mypy2                  | 349 ms                                                                 | 352 ms: 1.01x slower                                                              |
| xml_etree_parse        | 152 ms                                                                 | 153 ms: 1.01x slower                                                              |
| pathlib                | 17.7 ms                                                                | 17.9 ms: 1.01x slower                                                             |
| 2to3                   | 268 ms                                                                 | 271 ms: 1.01x slower                                                              |
| sqlglot_parse          | 1.33 ms                                                                | 1.34 ms: 1.01x slower                                                             |
| dulwich_log            | 67.7 ms                                                                | 68.3 ms: 1.01x slower                                                             |
| xml_etree_iterparse    | 103 ms                                                                 | 104 ms: 1.01x slower                                                              |
| sqlglot_transpile      | 1.65 ms                                                                | 1.67 ms: 1.01x slower                                                             |
| python_startup         | 9.06 ms                                                                | 9.15 ms: 1.01x slower                                                             |
| deepcopy               | 363 us                                                                 | 367 us: 1.01x slower                                                              |
| python_startup_no_site | 6.65 ms                                                                | 6.71 ms: 1.01x slower                                                             |
| pprint_pformat         | 1.50 sec                                                               | 1.51 sec: 1.01x slower                                                            |
| chaos                  | 68.6 ms                                                                | 69.3 ms: 1.01x slower                                                             |
| spectral_norm          | 102 ms                                                                 | 104 ms: 1.01x slower                                                              |
| pyflate                | 444 ms                                                                 | 449 ms: 1.01x slower                                                              |
| deepcopy_reduce        | 3.20 us                                                                | 3.24 us: 1.01x slower                                                             |
| regex_v8               | 22.1 ms                                                                | 22.4 ms: 1.01x slower                                                             |
| pycparser              | 1.15 sec                                                               | 1.16 sec: 1.01x slower                                                            |
| coverage               | 102 ms                                                                 | 103 ms: 1.02x slower                                                              |
| sqlglot_normalize      | 111 ms                                                                 | 113 ms: 1.02x slower                                                              |
| telco                  | 6.76 ms                                                                | 6.88 ms: 1.02x slower                                                             |
| fannkuch               | 374 ms                                                                 | 381 ms: 1.02x slower                                                              |
| async_generators       | 442 ms                                                                 | 451 ms: 1.02x slower                                                              |
| xml_etree_generate     | 84.0 ms                                                                | 85.8 ms: 1.02x slower                                                             |
| sqlglot_optimize       | 54.5 ms                                                                | 55.7 ms: 1.02x slower                                                             |
| sqlalchemy_imperative  | 18.7 ms                                                                | 19.3 ms: 1.03x slower                                                             |
| tornado_http           | 98.5 ms                                                                | 102 ms: 1.04x slower                                                              |
| xml_etree_process      | 58.2 ms                                                                | 60.4 ms: 1.04x slower                                                             |
| pickle                 | 10.3 us                                                                | 10.8 us: 1.05x slower                                                             |
| gc_traversal           | 3.94 ms                                                                | 4.19 ms: 1.06x slower                                                             |
| unpack_sequence        | 47.5 ns                                                                | 50.6 ns: 1.07x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (23): json, logging_simple, async_tree_cpu_io_mixed, richards, async_tree_memoization, mdp, scimark_fft, nqueens, async_tree_none, html5lib, bench_thread_pool, bench_mp_pool, dask, regex_compile, create_gc_cycles, json_loads, async_tree_io, meteor_contest, logging_format, genshi_xml, comprehensions, scimark_sparse_mat_mult, sqlalchemy_declarative
