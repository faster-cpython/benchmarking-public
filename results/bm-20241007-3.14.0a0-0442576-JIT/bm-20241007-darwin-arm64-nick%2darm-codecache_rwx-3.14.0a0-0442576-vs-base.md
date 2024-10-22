# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: darwin-arm64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.73x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 181 ms                                                                | 168 ms: 1.08x faster                                               |
| docutils       | 1.57 sec                                                              | 1.49 sec: 1.05x faster                                             |
| html5lib       | 33.9 ms                                                               | 32.6 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|---------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none_tg              | 196 ms                                                                | 186 ms: 1.06x faster                                               |
| async_tree_memoization          | 263 ms                                                                | 250 ms: 1.05x faster                                               |
| async_tree_eager_memoization_tg | 129 ms                                                                | 125 ms: 1.03x faster                                               |
| async_tree_eager                | 63.0 ms                                                               | 61.1 ms: 1.03x faster                                              |
| async_tree_eager_tg             | 41.4 ms                                                               | 41.2 ms: 1.01x faster                                              |
| async_generators                | 290 ms                                                                | 289 ms: 1.00x faster                                               |
| asyncio_websockets              | 242 ms                                                                | 241 ms: 1.00x faster                                               |
| async_tree_eager_memoization    | 153 ms                                                                | 157 ms: 1.02x slower                                               |
| async_tree_io_tg                | 541 ms                                                                | 565 ms: 1.05x slower                                               |
| async_tree_memoization_tg       | 246 ms                                                                | 259 ms: 1.05x slower                                               |
| Geometric mean                  | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (11): async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, coroutines, asyncio_tcp_ssl, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 63.6 ms                                                               | 63.5 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 76.1 ms                                                               | 71.8 ms: 1.06x faster                                              |
| regex_dna      | 148 ms                                                                | 148 ms: 1.00x slower                                               |
| regex_v8       | 16.8 ms                                                               | 17.0 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_list          | 3.01 us                                                               | 2.94 us: 1.02x faster                                              |
| xml_etree_iterparse  | 72.4 ms                                                               | 70.9 ms: 1.02x faster                                              |
| xml_etree_process    | 34.3 ms                                                               | 33.8 ms: 1.01x faster                                              |
| json_loads           | 16.5 us                                                               | 16.3 us: 1.01x faster                                              |
| tomli_loads          | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                             |
| pickle_pure_python   | 177 us                                                                | 175 us: 1.01x faster                                               |
| unpickle_pure_python | 131 us                                                                | 130 us: 1.01x faster                                               |
| pickle_dict          | 18.2 us                                                               | 18.1 us: 1.01x faster                                              |
| xml_etree_generate   | 49.4 ms                                                               | 49.2 ms: 1.00x faster                                              |
| unpickle             | 9.03 us                                                               | 9.06 us: 1.00x slower                                              |
| json_dumps           | 6.10 ms                                                               | 6.14 ms: 1.01x slower                                              |
| unpickle_list        | 2.97 us                                                               | 2.99 us: 1.01x slower                                              |
| pickle               | 7.36 us                                                               | 7.44 us: 1.01x slower                                              |
| xml_etree_parse      | 104 ms                                                                | 106 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 19.1 ms                                                               | 16.9 ms: 1.13x faster                                              |
| python_startup_no_site | 14.8 ms                                                               | 13.9 ms: 1.06x faster                                              |
| Geometric mean         | (ref)                                                                 | 1.09x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 42.4 ms                                                               | 31.8 ms: 1.33x faster                                              |
| django_template | 23.0 ms                                                               | 20.2 ms: 1.14x faster                                              |
| genshi_text     | 16.3 ms                                                               | 14.6 ms: 1.11x faster                                              |
| mako            | 6.41 ms                                                               | 6.39 ms: 1.00x faster                                              |
| Geometric mean  | (ref)                                                                 | 1.14x faster                                                       |

All benchmarks:
===============

| Benchmark                       | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|---------------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| create_gc_cycles                | 1.29 ms                                                               | 894 us: 1.44x faster                                               |
| genshi_xml                      | 42.4 ms                                                               | 31.8 ms: 1.33x faster                                              |
| bench_mp_pool                   | 62.2 ms                                                               | 50.7 ms: 1.23x faster                                              |
| go                              | 110 ms                                                                | 93.4 ms: 1.18x faster                                              |
| gc_traversal                    | 2.91 ms                                                               | 2.47 ms: 1.18x faster                                              |
| richards                        | 35.6 ms                                                               | 30.7 ms: 1.16x faster                                              |
| richards_super                  | 39.0 ms                                                               | 34.1 ms: 1.14x faster                                              |
| django_template                 | 23.0 ms                                                               | 20.2 ms: 1.14x faster                                              |
| python_startup                  | 19.1 ms                                                               | 16.9 ms: 1.13x faster                                              |
| hexiom                          | 4.96 ms                                                               | 4.42 ms: 1.12x faster                                              |
| genshi_text                     | 16.3 ms                                                               | 14.6 ms: 1.11x faster                                              |
| raytrace                        | 191 ms                                                                | 171 ms: 1.11x faster                                               |
| sqlglot_optimize                | 37.5 ms                                                               | 33.9 ms: 1.11x faster                                              |
| pprint_safe_repr                | 506 ms                                                                | 467 ms: 1.08x faster                                               |
| 2to3                            | 181 ms                                                                | 168 ms: 1.08x faster                                               |
| sqlglot_transpile               | 1.05 ms                                                               | 986 us: 1.07x faster                                               |
| sqlglot_normalize               | 187 ms                                                                | 175 ms: 1.07x faster                                               |
| python_startup_no_site          | 14.8 ms                                                               | 13.9 ms: 1.06x faster                                              |
| sympy_integrate                 | 12.5 ms                                                               | 11.8 ms: 1.06x faster                                              |
| regex_compile                   | 76.1 ms                                                               | 71.8 ms: 1.06x faster                                              |
| sqlglot_parse                   | 855 us                                                                | 808 us: 1.06x faster                                               |
| sympy_str                       | 150 ms                                                                | 142 ms: 1.06x faster                                               |
| async_tree_none_tg              | 196 ms                                                                | 186 ms: 1.06x faster                                               |
| async_tree_memoization          | 263 ms                                                                | 250 ms: 1.05x faster                                               |
| docutils                        | 1.57 sec                                                              | 1.49 sec: 1.05x faster                                             |
| sympy_sum                       | 78.3 ms                                                               | 74.5 ms: 1.05x faster                                              |
| pycparser                       | 682 ms                                                                | 649 ms: 1.05x faster                                               |
| deepcopy                        | 155 us                                                                | 148 us: 1.05x faster                                               |
| generators                      | 25.2 ms                                                               | 24.2 ms: 1.04x faster                                              |
| sympy_expand                    | 246 ms                                                                | 236 ms: 1.04x faster                                               |
| html5lib                        | 33.9 ms                                                               | 32.6 ms: 1.04x faster                                              |
| meteor_contest                  | 76.3 ms                                                               | 73.6 ms: 1.04x faster                                              |
| logging_format                  | 3.41 us                                                               | 3.30 us: 1.04x faster                                              |
| fannkuch                        | 269 ms                                                                | 260 ms: 1.03x faster                                               |
| chaos                           | 41.0 ms                                                               | 39.8 ms: 1.03x faster                                              |
| async_tree_eager_memoization_tg | 129 ms                                                                | 125 ms: 1.03x faster                                               |
| async_tree_eager                | 63.0 ms                                                               | 61.1 ms: 1.03x faster                                              |
| mdp                             | 1.50 sec                                                              | 1.46 sec: 1.03x faster                                             |
| spectral_norm                   | 68.7 ms                                                               | 66.9 ms: 1.03x faster                                              |
| deepcopy_memo                   | 16.7 us                                                               | 16.2 us: 1.03x faster                                              |
| deltablue                       | 2.42 ms                                                               | 2.36 ms: 1.03x faster                                              |
| pickle_list                     | 3.01 us                                                               | 2.94 us: 1.02x faster                                              |
| logging_simple                  | 3.10 us                                                               | 3.03 us: 1.02x faster                                              |
| pprint_pformat                  | 1.01 sec                                                              | 985 ms: 1.02x faster                                               |
| comprehensions                  | 12.8 us                                                               | 12.5 us: 1.02x faster                                              |
| xml_etree_iterparse             | 72.4 ms                                                               | 70.9 ms: 1.02x faster                                              |
| pyflate                         | 323 ms                                                                | 317 ms: 1.02x faster                                               |
| pathlib                         | 22.3 ms                                                               | 21.9 ms: 1.02x faster                                              |
| json                            | 2.89 ms                                                               | 2.85 ms: 1.02x faster                                              |
| xml_etree_process               | 34.3 ms                                                               | 33.8 ms: 1.01x faster                                              |
| json_loads                      | 16.5 us                                                               | 16.3 us: 1.01x faster                                              |
| tomli_loads                     | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                             |
| pickle_pure_python              | 177 us                                                                | 175 us: 1.01x faster                                               |
| bpe_tokeniser                   | 3.10 sec                                                              | 3.07 sec: 1.01x faster                                             |
| deepcopy_reduce                 | 1.51 us                                                               | 1.50 us: 1.01x faster                                              |
| unpickle_pure_python            | 131 us                                                                | 130 us: 1.01x faster                                               |
| dulwich_log                     | 29.0 ms                                                               | 28.7 ms: 1.01x faster                                              |
| unpack_sequence                 | 75.7 ns                                                               | 75.1 ns: 1.01x faster                                              |
| bench_thread_pool               | 480 us                                                                | 476 us: 1.01x faster                                               |
| pickle_dict                     | 18.2 us                                                               | 18.1 us: 1.01x faster                                              |
| coverage                        | 43.9 ms                                                               | 43.6 ms: 1.01x faster                                              |
| thrift                          | 420 us                                                                | 417 us: 1.01x faster                                               |
| async_tree_eager_tg             | 41.4 ms                                                               | 41.2 ms: 1.01x faster                                              |
| xml_etree_generate              | 49.4 ms                                                               | 49.2 ms: 1.00x faster                                              |
| scimark_fft                     | 185 ms                                                                | 184 ms: 1.00x faster                                               |
| async_generators                | 290 ms                                                                | 289 ms: 1.00x faster                                               |
| mako                            | 6.41 ms                                                               | 6.39 ms: 1.00x faster                                              |
| nbody                           | 63.6 ms                                                               | 63.5 ms: 1.00x faster                                              |
| asyncio_websockets              | 242 ms                                                                | 241 ms: 1.00x faster                                               |
| regex_dna                       | 148 ms                                                                | 148 ms: 1.00x slower                                               |
| unpickle                        | 9.03 us                                                               | 9.06 us: 1.00x slower                                              |
| json_dumps                      | 6.10 ms                                                               | 6.14 ms: 1.01x slower                                              |
| typing_runtime_protocols        | 95.0 us                                                               | 95.8 us: 1.01x slower                                              |
| unpickle_list                   | 2.97 us                                                               | 2.99 us: 1.01x slower                                              |
| nqueens                         | 57.1 ms                                                               | 57.7 ms: 1.01x slower                                              |
| pickle                          | 7.36 us                                                               | 7.44 us: 1.01x slower                                              |
| regex_v8                        | 16.8 ms                                                               | 17.0 ms: 1.01x slower                                              |
| telco                           | 4.50 ms                                                               | 4.57 ms: 1.02x slower                                              |
| scimark_sor                     | 85.8 ms                                                               | 87.4 ms: 1.02x slower                                              |
| xml_etree_parse                 | 104 ms                                                                | 106 ms: 1.02x slower                                               |
| async_tree_eager_memoization    | 153 ms                                                                | 157 ms: 1.02x slower                                               |
| scimark_monte_carlo             | 45.1 ms                                                               | 46.2 ms: 1.03x slower                                              |
| async_tree_io_tg                | 541 ms                                                                | 565 ms: 1.05x slower                                               |
| async_tree_memoization_tg       | 246 ms                                                                | 259 ms: 1.05x slower                                               |
| logging_silent                  | 56.4 ns                                                               | 60.9 ns: 1.08x slower                                              |
| Geometric mean                  | (ref)                                                                 | 1.03x faster                                                       |

Benchmark hidden because not significant (20): pylint, tornado_http, async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, pidigits, scimark_lu, sqlite_synth, regex_effbot, coroutines, scimark_sparse_mat_mult, float, crypto_pyaes, asyncio_tcp_ssl, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, asyncio_tcp
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.73x