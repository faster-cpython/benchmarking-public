# Results vs. base

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.043x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                                                                          | 176 ms: 1.09x slower                                                                                                |
| docutils       | 1.43 sec                                                                                                        | 1.56 sec: 1.09x slower                                                                                              |
| html5lib       | 30.0 ms                                                                                                         | 33.8 ms: 1.13x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.08x slower                                                                                                        |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|-------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| coroutines                    | 16.1 ms                                                                                                         | 16.0 ms: 1.01x faster                                                                                               |
| async_tree_cpu_io_mixed_tg    | 459 ms                                                                                                          | 461 ms: 1.00x slower                                                                                                |
| async_tree_eager_cpu_io_mixed | 357 ms                                                                                                          | 361 ms: 1.01x slower                                                                                                |
| async_tree_eager_tg           | 41.9 ms                                                                                                         | 42.4 ms: 1.01x slower                                                                                               |
| async_tree_io                 | 579 ms                                                                                                          | 589 ms: 1.02x slower                                                                                                |
| async_tree_eager_memoization  | 151 ms                                                                                                          | 156 ms: 1.03x slower                                                                                                |
| async_generators              | 278 ms                                                                                                          | 290 ms: 1.04x slower                                                                                                |
| async_tree_eager              | 60.6 ms                                                                                                         | 63.7 ms: 1.05x slower                                                                                               |
| Geometric mean                | (ref)                                                                                                           | 1.01x slower                                                                                                        |

Benchmark hidden because not significant (13): async_tree_eager_io_tg, asyncio_websockets, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, async_tree_eager_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_memoization_tg, asyncio_tcp, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| float          | 48.4 ms                                                                                                         | 46.1 ms: 1.05x faster                                                                                               |
| nbody          | 60.1 ms                                                                                                         | 63.6 ms: 1.06x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.00x slower                                                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.53 ms                                                                                                         | 2.49 ms: 1.02x faster                                                                                               |
| regex_v8       | 16.8 ms                                                                                                         | 16.6 ms: 1.01x faster                                                                                               |
| regex_dna      | 146 ms                                                                                                          | 148 ms: 1.01x slower                                                                                                |
| regex_compile  | 67.2 ms                                                                                                         | 74.3 ms: 1.10x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.02x slower                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                                                                        | 1.25 sec: 1.18x faster                                                                                              |
| xml_etree_process    | 37.5 ms                                                                                                         | 34.1 ms: 1.10x faster                                                                                               |
| unpickle_pure_python | 141 us                                                                                                          | 131 us: 1.08x faster                                                                                                |
| xml_etree_generate   | 52.6 ms                                                                                                         | 50.1 ms: 1.05x faster                                                                                               |
| pickle_list          | 2.99 us                                                                                                         | 2.92 us: 1.03x faster                                                                                               |
| pickle_pure_python   | 182 us                                                                                                          | 178 us: 1.02x faster                                                                                                |
| xml_etree_iterparse  | 73.7 ms                                                                                                         | 72.3 ms: 1.02x faster                                                                                               |
| unpickle_list        | 2.94 us                                                                                                         | 2.88 us: 1.02x faster                                                                                               |
| json_dumps           | 6.31 ms                                                                                                         | 6.19 ms: 1.02x faster                                                                                               |
| pickle_dict          | 18.2 us                                                                                                         | 18.3 us: 1.00x slower                                                                                               |
| pickle               | 7.39 us                                                                                                         | 7.42 us: 1.00x slower                                                                                               |
| unpickle             | 9.12 us                                                                                                         | 9.23 us: 1.01x slower                                                                                               |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                                                                         | 14.4 ms: 1.04x slower                                                                                               |
| python_startup_no_site | 11.0 ms                                                                                                         | 11.5 ms: 1.05x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.05x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.06 ms                                                                                                         | 6.45 ms: 1.09x faster                                                                                               |
| django_template | 20.1 ms                                                                                                         | 22.6 ms: 1.12x slower                                                                                               |
| genshi_text     | 13.7 ms                                                                                                         | 16.6 ms: 1.21x slower                                                                                               |
| genshi_xml      | 30.0 ms                                                                                                         | 41.1 ms: 1.37x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.14x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                     | results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|-------------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                   | 1.47 sec                                                                                                        | 1.25 sec: 1.18x faster                                                                                              |
| xml_etree_process             | 37.5 ms                                                                                                         | 34.1 ms: 1.10x faster                                                                                               |
| mako                          | 7.06 ms                                                                                                         | 6.45 ms: 1.09x faster                                                                                               |
| unpickle_pure_python          | 141 us                                                                                                          | 131 us: 1.08x faster                                                                                                |
| scimark_sor                   | 93.1 ms                                                                                                         | 87.7 ms: 1.06x faster                                                                                               |
| xml_etree_generate            | 52.6 ms                                                                                                         | 50.1 ms: 1.05x faster                                                                                               |
| float                         | 48.4 ms                                                                                                         | 46.1 ms: 1.05x faster                                                                                               |
| deepcopy_memo                 | 16.7 us                                                                                                         | 16.1 us: 1.04x faster                                                                                               |
| pathlib                       | 23.6 ms                                                                                                         | 22.9 ms: 1.03x faster                                                                                               |
| pickle_list                   | 2.99 us                                                                                                         | 2.92 us: 1.03x faster                                                                                               |
| pickle_pure_python            | 182 us                                                                                                          | 178 us: 1.02x faster                                                                                                |
| scimark_lu                    | 64.8 ms                                                                                                         | 63.4 ms: 1.02x faster                                                                                               |
| xml_etree_iterparse           | 73.7 ms                                                                                                         | 72.3 ms: 1.02x faster                                                                                               |
| unpickle_list                 | 2.94 us                                                                                                         | 2.88 us: 1.02x faster                                                                                               |
| regex_effbot                  | 2.53 ms                                                                                                         | 2.49 ms: 1.02x faster                                                                                               |
| json_dumps                    | 6.31 ms                                                                                                         | 6.19 ms: 1.02x faster                                                                                               |
| bpe_tokeniser                 | 3.12 sec                                                                                                        | 3.07 sec: 1.02x faster                                                                                              |
| regex_v8                      | 16.8 ms                                                                                                         | 16.6 ms: 1.01x faster                                                                                               |
| coroutines                    | 16.1 ms                                                                                                         | 16.0 ms: 1.01x faster                                                                                               |
| async_tree_cpu_io_mixed_tg    | 459 ms                                                                                                          | 461 ms: 1.00x slower                                                                                                |
| pickle_dict                   | 18.2 us                                                                                                         | 18.3 us: 1.00x slower                                                                                               |
| fannkuch                      | 262 ms                                                                                                          | 263 ms: 1.00x slower                                                                                                |
| pickle                        | 7.39 us                                                                                                         | 7.42 us: 1.00x slower                                                                                               |
| deepcopy_reduce               | 1.50 us                                                                                                         | 1.51 us: 1.01x slower                                                                                               |
| async_tree_eager_cpu_io_mixed | 357 ms                                                                                                          | 361 ms: 1.01x slower                                                                                                |
| thrift                        | 420 us                                                                                                          | 425 us: 1.01x slower                                                                                                |
| coverage                      | 44.3 ms                                                                                                         | 44.8 ms: 1.01x slower                                                                                               |
| regex_dna                     | 146 ms                                                                                                          | 148 ms: 1.01x slower                                                                                                |
| unpickle                      | 9.12 us                                                                                                         | 9.23 us: 1.01x slower                                                                                               |
| async_tree_eager_tg           | 41.9 ms                                                                                                         | 42.4 ms: 1.01x slower                                                                                               |
| telco                         | 4.74 ms                                                                                                         | 4.80 ms: 1.01x slower                                                                                               |
| spectral_norm                 | 66.0 ms                                                                                                         | 67.0 ms: 1.01x slower                                                                                               |
| async_tree_io                 | 579 ms                                                                                                          | 589 ms: 1.02x slower                                                                                                |
| pyflate                       | 320 ms                                                                                                          | 326 ms: 1.02x slower                                                                                                |
| mdp                           | 1.43 sec                                                                                                        | 1.46 sec: 1.02x slower                                                                                              |
| typing_runtime_protocols      | 92.2 us                                                                                                         | 94.3 us: 1.02x slower                                                                                               |
| scimark_fft                   | 179 ms                                                                                                          | 184 ms: 1.03x slower                                                                                                |
| bench_mp_pool                 | 48.1 ms                                                                                                         | 49.4 ms: 1.03x slower                                                                                               |
| async_tree_eager_memoization  | 151 ms                                                                                                          | 156 ms: 1.03x slower                                                                                                |
| crypto_pyaes                  | 50.2 ms                                                                                                         | 51.7 ms: 1.03x slower                                                                                               |
| sqlite_synth                  | 1.54 us                                                                                                         | 1.58 us: 1.03x slower                                                                                               |
| logging_silent                | 60.9 ns                                                                                                         | 62.8 ns: 1.03x slower                                                                                               |
| bench_thread_pool             | 452 us                                                                                                          | 469 us: 1.04x slower                                                                                                |
| async_generators              | 278 ms                                                                                                          | 290 ms: 1.04x slower                                                                                                |
| python_startup                | 13.9 ms                                                                                                         | 14.4 ms: 1.04x slower                                                                                               |
| meteor_contest                | 71.6 ms                                                                                                         | 75.2 ms: 1.05x slower                                                                                               |
| async_tree_eager              | 60.6 ms                                                                                                         | 63.7 ms: 1.05x slower                                                                                               |
| deepcopy                      | 146 us                                                                                                          | 153 us: 1.05x slower                                                                                                |
| python_startup_no_site        | 11.0 ms                                                                                                         | 11.5 ms: 1.05x slower                                                                                               |
| nbody                         | 60.1 ms                                                                                                         | 63.6 ms: 1.06x slower                                                                                               |
| pycparser                     | 639 ms                                                                                                          | 678 ms: 1.06x slower                                                                                                |
| dulwich_log                   | 27.1 ms                                                                                                         | 29.0 ms: 1.07x slower                                                                                               |
| docutils                      | 1.43 sec                                                                                                        | 1.56 sec: 1.09x slower                                                                                              |
| sympy_expand                  | 226 ms                                                                                                          | 247 ms: 1.09x slower                                                                                                |
| sympy_str                     | 131 ms                                                                                                          | 143 ms: 1.09x slower                                                                                                |
| 2to3                          | 161 ms                                                                                                          | 176 ms: 1.09x slower                                                                                                |
| sympy_sum                     | 68.8 ms                                                                                                         | 75.2 ms: 1.09x slower                                                                                               |
| nqueens                       | 53.2 ms                                                                                                         | 58.2 ms: 1.09x slower                                                                                               |
| deltablue                     | 2.14 ms                                                                                                         | 2.35 ms: 1.10x slower                                                                                               |
| sqlglot_normalize             | 167 ms                                                                                                          | 183 ms: 1.10x slower                                                                                                |
| scimark_sparse_mat_mult       | 2.70 ms                                                                                                         | 2.98 ms: 1.10x slower                                                                                               |
| regex_compile                 | 67.2 ms                                                                                                         | 74.3 ms: 1.10x slower                                                                                               |
| pprint_safe_repr              | 458 ms                                                                                                          | 509 ms: 1.11x slower                                                                                                |
| scimark_monte_carlo           | 42.6 ms                                                                                                         | 47.4 ms: 1.11x slower                                                                                               |
| pprint_pformat                | 932 ms                                                                                                          | 1.04 sec: 1.12x slower                                                                                              |
| sympy_integrate               | 10.3 ms                                                                                                         | 11.5 ms: 1.12x slower                                                                                               |
| django_template               | 20.1 ms                                                                                                         | 22.6 ms: 1.12x slower                                                                                               |
| chaos                         | 35.6 ms                                                                                                         | 40.1 ms: 1.13x slower                                                                                               |
| html5lib                      | 30.0 ms                                                                                                         | 33.8 ms: 1.13x slower                                                                                               |
| pylint                        | 181 ms                                                                                                          | 205 ms: 1.13x slower                                                                                                |
| sqlglot_optimize              | 31.0 ms                                                                                                         | 35.5 ms: 1.14x slower                                                                                               |
| sqlglot_transpile             | 900 us                                                                                                          | 1.04 ms: 1.15x slower                                                                                               |
| sqlglot_parse                 | 737 us                                                                                                          | 850 us: 1.15x slower                                                                                                |
| raytrace                      | 149 ms                                                                                                          | 173 ms: 1.16x slower                                                                                                |
| hexiom                        | 4.05 ms                                                                                                         | 4.74 ms: 1.17x slower                                                                                               |
| comprehensions                | 10.9 us                                                                                                         | 12.8 us: 1.18x slower                                                                                               |
| generators                    | 20.7 ms                                                                                                         | 24.6 ms: 1.19x slower                                                                                               |
| genshi_text                   | 13.7 ms                                                                                                         | 16.6 ms: 1.21x slower                                                                                               |
| go                            | 79.1 ms                                                                                                         | 101 ms: 1.28x slower                                                                                                |
| richards_super                | 35.9 ms                                                                                                         | 46.4 ms: 1.29x slower                                                                                               |
| genshi_xml                    | 30.0 ms                                                                                                         | 41.1 ms: 1.37x slower                                                                                               |
| richards                      | 32.0 ms                                                                                                         | 44.4 ms: 1.39x slower                                                                                               |
| unpack_sequence               | 26.6 ns                                                                                                         | 75.9 ns: 2.86x slower                                                                                               |
| Geometric mean                | (ref)                                                                                                           | 1.05x slower                                                                                                        |

Benchmark hidden because not significant (22): xml_etree_parse, pidigits, logging_format, async_tree_eager_io_tg, gc_traversal, json, asyncio_websockets, logging_simple, asyncio_tcp_ssl, json_loads, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, create_gc_cycles, async_tree_eager_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_memoization_tg, asyncio_tcp, async_tree_io_tg, async_tree_none, tornado_http

- Geometric mean (including insignificant results): 1.043x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x