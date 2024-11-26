# Results vs. base

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.050x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                                                                          | 181 ms: 1.12x slower                                                                                                |
| docutils       | 1.40 sec                                                                                                        | 1.60 sec: 1.15x slower                                                                                              |
| html5lib       | 31.9 ms                                                                                                         | 34.2 ms: 1.07x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.09x slower                                                                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|-------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| coroutines                    | 16.4 ms                                                                                                         | 16.2 ms: 1.01x faster                                                                                               |
| async_tree_cpu_io_mixed_tg    | 460 ms                                                                                                          | 458 ms: 1.00x faster                                                                                                |
| asyncio_websockets            | 241 ms                                                                                                          | 242 ms: 1.00x slower                                                                                                |
| async_tree_eager_tg           | 41.2 ms                                                                                                         | 41.6 ms: 1.01x slower                                                                                               |
| async_tree_eager_cpu_io_mixed | 359 ms                                                                                                          | 364 ms: 1.01x slower                                                                                                |
| async_tree_eager_memoization  | 154 ms                                                                                                          | 158 ms: 1.03x slower                                                                                                |
| async_generators              | 274 ms                                                                                                          | 291 ms: 1.06x slower                                                                                                |
| async_tree_eager              | 59.3 ms                                                                                                         | 63.5 ms: 1.07x slower                                                                                               |
| async_tree_io_tg              | 529 ms                                                                                                          | 573 ms: 1.08x slower                                                                                                |
| Geometric mean                | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (12): asyncio_tcp, async_tree_io, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_io, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 48.8 ms                                                                                                         | 46.7 ms: 1.04x faster                                                                                               |
| nbody          | 65.7 ms                                                                                                         | 63.6 ms: 1.03x faster                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                                                                          | 149 ms: 1.01x slower                                                                                                |
| regex_effbot   | 2.62 ms                                                                                                         | 2.64 ms: 1.01x slower                                                                                               |
| regex_v8       | 16.4 ms                                                                                                         | 16.9 ms: 1.03x slower                                                                                               |
| regex_compile  | 67.8 ms                                                                                                         | 76.0 ms: 1.12x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.04x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.51 sec                                                                                                        | 1.26 sec: 1.20x faster                                                                                              |
| xml_etree_process    | 37.4 ms                                                                                                         | 34.6 ms: 1.08x faster                                                                                               |
| unpickle_pure_python | 140 us                                                                                                          | 130 us: 1.08x faster                                                                                                |
| xml_etree_generate   | 52.3 ms                                                                                                         | 50.1 ms: 1.04x faster                                                                                               |
| xml_etree_iterparse  | 73.1 ms                                                                                                         | 70.7 ms: 1.03x faster                                                                                               |
| xml_etree_parse      | 107 ms                                                                                                          | 104 ms: 1.03x faster                                                                                                |
| pickle_pure_python   | 182 us                                                                                                          | 176 us: 1.03x faster                                                                                                |
| pickle_list          | 3.00 us                                                                                                         | 2.97 us: 1.01x faster                                                                                               |
| json_dumps           | 6.20 ms                                                                                                         | 6.14 ms: 1.01x faster                                                                                               |
| unpickle             | 9.07 us                                                                                                         | 9.01 us: 1.01x faster                                                                                               |
| pickle_dict          | 18.2 us                                                                                                         | 18.1 us: 1.00x faster                                                                                               |
| pickle               | 7.33 us                                                                                                         | 7.43 us: 1.01x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.04x faster                                                                                                        |

Benchmark hidden because not significant (2): unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.3 ms                                                                                                         | 18.2 ms: 1.11x slower                                                                                               |
| python_startup_no_site | 13.3 ms                                                                                                         | 15.2 ms: 1.14x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.13x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.83 ms                                                                                                         | 6.39 ms: 1.07x faster                                                                                               |
| django_template | 19.7 ms                                                                                                         | 23.4 ms: 1.19x slower                                                                                               |
| genshi_text     | 13.6 ms                                                                                                         | 17.2 ms: 1.26x slower                                                                                               |
| genshi_xml      | 29.7 ms                                                                                                         | 42.7 ms: 1.43x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.19x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                     | results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json | results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json |
|-------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                   | 1.51 sec                                                                                                        | 1.26 sec: 1.20x faster                                                                                              |
| scimark_sor                   | 95.5 ms                                                                                                         | 87.3 ms: 1.09x faster                                                                                               |
| xml_etree_process             | 37.4 ms                                                                                                         | 34.6 ms: 1.08x faster                                                                                               |
| unpickle_pure_python          | 140 us                                                                                                          | 130 us: 1.08x faster                                                                                                |
| mako                          | 6.83 ms                                                                                                         | 6.39 ms: 1.07x faster                                                                                               |
| spectral_norm                 | 70.3 ms                                                                                                         | 67.0 ms: 1.05x faster                                                                                               |
| float                         | 48.8 ms                                                                                                         | 46.7 ms: 1.04x faster                                                                                               |
| xml_etree_generate            | 52.3 ms                                                                                                         | 50.1 ms: 1.04x faster                                                                                               |
| xml_etree_iterparse           | 73.1 ms                                                                                                         | 70.7 ms: 1.03x faster                                                                                               |
| xml_etree_parse               | 107 ms                                                                                                          | 104 ms: 1.03x faster                                                                                                |
| nbody                         | 65.7 ms                                                                                                         | 63.6 ms: 1.03x faster                                                                                               |
| pickle_pure_python            | 182 us                                                                                                          | 176 us: 1.03x faster                                                                                                |
| bpe_tokeniser                 | 3.13 sec                                                                                                        | 3.07 sec: 1.02x faster                                                                                              |
| scimark_lu                    | 65.2 ms                                                                                                         | 64.0 ms: 1.02x faster                                                                                               |
| telco                         | 4.56 ms                                                                                                         | 4.49 ms: 1.01x faster                                                                                               |
| logging_silent                | 61.5 ns                                                                                                         | 60.7 ns: 1.01x faster                                                                                               |
| scimark_fft                   | 187 ms                                                                                                          | 184 ms: 1.01x faster                                                                                                |
| deepcopy_memo                 | 16.7 us                                                                                                         | 16.5 us: 1.01x faster                                                                                               |
| pickle_list                   | 3.00 us                                                                                                         | 2.97 us: 1.01x faster                                                                                               |
| json_dumps                    | 6.20 ms                                                                                                         | 6.14 ms: 1.01x faster                                                                                               |
| pyflate                       | 325 ms                                                                                                          | 323 ms: 1.01x faster                                                                                                |
| unpickle                      | 9.07 us                                                                                                         | 9.01 us: 1.01x faster                                                                                               |
| coroutines                    | 16.4 ms                                                                                                         | 16.2 ms: 1.01x faster                                                                                               |
| async_tree_cpu_io_mixed_tg    | 460 ms                                                                                                          | 458 ms: 1.00x faster                                                                                                |
| pickle_dict                   | 18.2 us                                                                                                         | 18.1 us: 1.00x faster                                                                                               |
| gc_traversal                  | 2.47 ms                                                                                                         | 2.47 ms: 1.00x faster                                                                                               |
| asyncio_websockets            | 241 ms                                                                                                          | 242 ms: 1.00x slower                                                                                                |
| fannkuch                      | 263 ms                                                                                                          | 265 ms: 1.01x slower                                                                                                |
| coverage                      | 43.7 ms                                                                                                         | 44.0 ms: 1.01x slower                                                                                               |
| thrift                        | 416 us                                                                                                          | 419 us: 1.01x slower                                                                                                |
| regex_dna                     | 148 ms                                                                                                          | 149 ms: 1.01x slower                                                                                                |
| regex_effbot                  | 2.62 ms                                                                                                         | 2.64 ms: 1.01x slower                                                                                               |
| logging_format                | 3.32 us                                                                                                         | 3.35 us: 1.01x slower                                                                                               |
| async_tree_eager_tg           | 41.2 ms                                                                                                         | 41.6 ms: 1.01x slower                                                                                               |
| deepcopy_reduce               | 1.50 us                                                                                                         | 1.52 us: 1.01x slower                                                                                               |
| logging_simple                | 3.04 us                                                                                                         | 3.08 us: 1.01x slower                                                                                               |
| async_tree_eager_cpu_io_mixed | 359 ms                                                                                                          | 364 ms: 1.01x slower                                                                                                |
| pickle                        | 7.33 us                                                                                                         | 7.43 us: 1.01x slower                                                                                               |
| sqlite_synth                  | 1.50 us                                                                                                         | 1.53 us: 1.01x slower                                                                                               |
| crypto_pyaes                  | 51.3 ms                                                                                                         | 52.3 ms: 1.02x slower                                                                                               |
| json                          | 2.82 ms                                                                                                         | 2.88 ms: 1.02x slower                                                                                               |
| async_tree_eager_memoization  | 154 ms                                                                                                          | 158 ms: 1.03x slower                                                                                                |
| typing_runtime_protocols      | 92.8 us                                                                                                         | 95.5 us: 1.03x slower                                                                                               |
| mdp                           | 1.44 sec                                                                                                        | 1.48 sec: 1.03x slower                                                                                              |
| regex_v8                      | 16.4 ms                                                                                                         | 16.9 ms: 1.03x slower                                                                                               |
| pathlib                       | 21.4 ms                                                                                                         | 22.2 ms: 1.03x slower                                                                                               |
| meteor_contest                | 71.6 ms                                                                                                         | 75.1 ms: 1.05x slower                                                                                               |
| bench_mp_pool                 | 48.6 ms                                                                                                         | 51.4 ms: 1.06x slower                                                                                               |
| bench_thread_pool             | 455 us                                                                                                          | 482 us: 1.06x slower                                                                                                |
| dulwich_log                   | 27.4 ms                                                                                                         | 29.0 ms: 1.06x slower                                                                                               |
| async_generators              | 274 ms                                                                                                          | 291 ms: 1.06x slower                                                                                                |
| async_tree_eager              | 59.3 ms                                                                                                         | 63.5 ms: 1.07x slower                                                                                               |
| html5lib                      | 31.9 ms                                                                                                         | 34.2 ms: 1.07x slower                                                                                               |
| pycparser                     | 632 ms                                                                                                          | 679 ms: 1.08x slower                                                                                                |
| async_tree_io_tg              | 529 ms                                                                                                          | 573 ms: 1.08x slower                                                                                                |
| pprint_pformat                | 936 ms                                                                                                          | 1.01 sec: 1.08x slower                                                                                              |
| scimark_sparse_mat_mult       | 2.75 ms                                                                                                         | 2.99 ms: 1.09x slower                                                                                               |
| deltablue                     | 2.22 ms                                                                                                         | 2.41 ms: 1.09x slower                                                                                               |
| pprint_safe_repr              | 458 ms                                                                                                          | 501 ms: 1.09x slower                                                                                                |
| scimark_monte_carlo           | 43.7 ms                                                                                                         | 47.8 ms: 1.09x slower                                                                                               |
| sympy_expand                  | 224 ms                                                                                                          | 246 ms: 1.10x slower                                                                                                |
| deepcopy                      | 144 us                                                                                                          | 157 us: 1.10x slower                                                                                                |
| python_startup                | 16.3 ms                                                                                                         | 18.2 ms: 1.11x slower                                                                                               |
| regex_compile                 | 67.8 ms                                                                                                         | 76.0 ms: 1.12x slower                                                                                               |
| 2to3                          | 161 ms                                                                                                          | 181 ms: 1.12x slower                                                                                                |
| chaos                         | 36.0 ms                                                                                                         | 40.5 ms: 1.12x slower                                                                                               |
| nqueens                       | 52.2 ms                                                                                                         | 59.0 ms: 1.13x slower                                                                                               |
| sqlglot_normalize             | 166 ms                                                                                                          | 188 ms: 1.13x slower                                                                                                |
| sympy_str                     | 132 ms                                                                                                          | 150 ms: 1.14x slower                                                                                                |
| python_startup_no_site        | 13.3 ms                                                                                                         | 15.2 ms: 1.14x slower                                                                                               |
| docutils                      | 1.40 sec                                                                                                        | 1.60 sec: 1.15x slower                                                                                              |
| sympy_sum                     | 68.8 ms                                                                                                         | 78.9 ms: 1.15x slower                                                                                               |
| sqlglot_parse                 | 736 us                                                                                                          | 848 us: 1.15x slower                                                                                                |
| hexiom                        | 4.08 ms                                                                                                         | 4.70 ms: 1.15x slower                                                                                               |
| sympy_integrate               | 10.9 ms                                                                                                         | 12.6 ms: 1.16x slower                                                                                               |
| sqlglot_transpile             | 899 us                                                                                                          | 1.05 ms: 1.16x slower                                                                                               |
| raytrace                      | 151 ms                                                                                                          | 177 ms: 1.17x slower                                                                                                |
| comprehensions                | 10.9 us                                                                                                         | 12.9 us: 1.18x slower                                                                                               |
| django_template               | 19.7 ms                                                                                                         | 23.4 ms: 1.19x slower                                                                                               |
| pylint                        | 178 ms                                                                                                          | 214 ms: 1.20x slower                                                                                                |
| sqlglot_optimize              | 30.8 ms                                                                                                         | 37.8 ms: 1.23x slower                                                                                               |
| go                            | 81.6 ms                                                                                                         | 101 ms: 1.24x slower                                                                                                |
| generators                    | 20.6 ms                                                                                                         | 25.4 ms: 1.24x slower                                                                                               |
| genshi_text                   | 13.6 ms                                                                                                         | 17.2 ms: 1.26x slower                                                                                               |
| richards_super                | 35.0 ms                                                                                                         | 46.6 ms: 1.33x slower                                                                                               |
| richards                      | 31.6 ms                                                                                                         | 45.2 ms: 1.43x slower                                                                                               |
| genshi_xml                    | 29.7 ms                                                                                                         | 42.7 ms: 1.43x slower                                                                                               |
| unpack_sequence               | 28.1 ns                                                                                                         | 76.8 ns: 2.73x slower                                                                                               |
| Geometric mean                | (ref)                                                                                                           | 1.06x slower                                                                                                        |

Benchmark hidden because not significant (17): asyncio_tcp, async_tree_io, unpickle_list, create_gc_cycles, pidigits, json_loads, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_io, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_memoization, async_tree_none, tornado_http

- Geometric mean (including insignificant results): 1.050x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x