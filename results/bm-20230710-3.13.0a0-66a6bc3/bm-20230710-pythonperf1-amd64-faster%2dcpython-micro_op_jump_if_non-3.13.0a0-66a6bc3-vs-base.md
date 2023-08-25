
# Results vs. base

- fork: faster-cpython
- ref: micro_op_jump_if_non
- machine: windows-amd64
- commit hash: 66a6bc3
- commit date: 2023-07-10
- overall geometric mean: 1.00x slower
- HPT reliability: 51.01%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tornado_http   | 98.7 ms                                                                    | 101 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                                     | 150 ms: 1.00x faster                                                                 |
| nbody          | 75.9 ms                                                                    | 77.8 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.61 ms                                                                    | 1.59 ms: 1.02x faster                                                                |
| regex_dna      | 121 ms                                                                     | 120 ms: 1.01x faster                                                                 |
| regex_compile  | 93.5 ms                                                                    | 93.1 ms: 1.00x faster                                                                |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_list        | 2.94 us                                                                    | 2.81 us: 1.05x faster                                                                |
| pickle               | 7.12 us                                                                    | 6.96 us: 1.02x faster                                                                |
| json_dumps           | 5.77 ms                                                                    | 5.68 ms: 1.02x faster                                                                |
| json_loads           | 13.6 us                                                                    | 13.5 us: 1.01x faster                                                                |
| pickle_pure_python   | 200 us                                                                     | 198 us: 1.01x faster                                                                 |
| pickle_list          | 2.82 us                                                                    | 2.84 us: 1.01x slower                                                                |
| unpickle_pure_python | 141 us                                                                     | 143 us: 1.01x slower                                                                 |
| xml_etree_iterparse  | 64.4 ms                                                                    | 65.4 ms: 1.02x slower                                                                |
| xml_etree_process    | 38.8 ms                                                                    | 39.5 ms: 1.02x slower                                                                |
| xml_etree_parse      | 91.2 ms                                                                    | 93.9 ms: 1.03x slower                                                                |
| xml_etree_generate   | 55.9 ms                                                                    | 57.7 ms: 1.03x slower                                                                |
| tomli_loads          | 1.59 sec                                                                   | 1.65 sec: 1.04x slower                                                               |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230710-pythonperf1-amd64-python-22988c323ad621b9f47b-3.13.0a0-22988c3 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl          | 2.20 sec                                                                   | 2.08 sec: 1.06x faster                                                               |
| unpickle_list            | 2.94 us                                                                    | 2.81 us: 1.05x faster                                                                |
| typing_runtime_protocols | 96.7 us                                                                    | 93.6 us: 1.03x faster                                                                |
| scimark_sor              | 84.4 ms                                                                    | 82.3 ms: 1.03x faster                                                                |
| pickle                   | 7.12 us                                                                    | 6.96 us: 1.02x faster                                                                |
| coroutines               | 15.5 ms                                                                    | 15.1 ms: 1.02x faster                                                                |
| unpack_sequence          | 41.1 ns                                                                    | 40.3 ns: 1.02x faster                                                                |
| dulwich_log              | 45.8 ms                                                                    | 44.9 ms: 1.02x faster                                                                |
| deepcopy_memo            | 25.7 us                                                                    | 25.2 us: 1.02x faster                                                                |
| go                       | 98.4 ms                                                                    | 96.6 ms: 1.02x faster                                                                |
| regex_effbot             | 1.61 ms                                                                    | 1.59 ms: 1.02x faster                                                                |
| json_dumps               | 5.77 ms                                                                    | 5.68 ms: 1.02x faster                                                                |
| fannkuch                 | 257 ms                                                                     | 253 ms: 1.01x faster                                                                 |
| async_generators         | 243 ms                                                                     | 240 ms: 1.01x faster                                                                 |
| scimark_lu               | 61.8 ms                                                                    | 61.1 ms: 1.01x faster                                                                |
| dask                     | 388 ms                                                                     | 383 ms: 1.01x faster                                                                 |
| sqlglot_parse            | 875 us                                                                     | 864 us: 1.01x faster                                                                 |
| json_loads               | 13.6 us                                                                    | 13.5 us: 1.01x faster                                                                |
| pickle_pure_python       | 200 us                                                                     | 198 us: 1.01x faster                                                                 |
| pyflate                  | 315 ms                                                                     | 312 ms: 1.01x faster                                                                 |
| deepcopy                 | 249 us                                                                     | 247 us: 1.01x faster                                                                 |
| sqlglot_transpile        | 1.10 ms                                                                    | 1.09 ms: 1.01x faster                                                                |
| richards_super           | 34.2 ms                                                                    | 33.9 ms: 1.01x faster                                                                |
| coverage                 | 51.5 ms                                                                    | 51.2 ms: 1.01x faster                                                                |
| spectral_norm            | 66.3 ms                                                                    | 65.9 ms: 1.01x faster                                                                |
| regex_dna                | 121 ms                                                                     | 120 ms: 1.01x faster                                                                 |
| regex_compile            | 93.5 ms                                                                    | 93.1 ms: 1.00x faster                                                                |
| sqlglot_optimize         | 36.0 ms                                                                    | 35.8 ms: 1.00x faster                                                                |
| mypy2                    | 223 ms                                                                     | 222 ms: 1.00x faster                                                                 |
| pidigits                 | 150 ms                                                                     | 150 ms: 1.00x faster                                                                 |
| hexiom                   | 4.39 ms                                                                    | 4.42 ms: 1.01x slower                                                                |
| logging_format           | 7.30 us                                                                    | 7.35 us: 1.01x slower                                                                |
| logging_silent           | 64.4 ns                                                                    | 64.8 ns: 1.01x slower                                                                |
| pickle_list              | 2.82 us                                                                    | 2.84 us: 1.01x slower                                                                |
| unpickle_pure_python     | 141 us                                                                     | 143 us: 1.01x slower                                                                 |
| logging_simple           | 6.78 us                                                                    | 6.84 us: 1.01x slower                                                                |
| sqlite_synth             | 1.76 us                                                                    | 1.77 us: 1.01x slower                                                                |
| raytrace                 | 182 ms                                                                     | 183 ms: 1.01x slower                                                                 |
| crypto_pyaes             | 45.4 ms                                                                    | 45.9 ms: 1.01x slower                                                                |
| json                     | 2.83 ms                                                                    | 2.87 ms: 1.01x slower                                                                |
| xml_etree_iterparse      | 64.4 ms                                                                    | 65.4 ms: 1.02x slower                                                                |
| generators               | 24.6 ms                                                                    | 25.1 ms: 1.02x slower                                                                |
| xml_etree_process        | 38.8 ms                                                                    | 39.5 ms: 1.02x slower                                                                |
| pprint_pformat           | 1.09 sec                                                                   | 1.11 sec: 1.02x slower                                                               |
| pprint_safe_repr         | 532 ms                                                                     | 543 ms: 1.02x slower                                                                 |
| tornado_http             | 98.7 ms                                                                    | 101 ms: 1.02x slower                                                                 |
| nbody                    | 75.9 ms                                                                    | 77.8 ms: 1.02x slower                                                                |
| mdp                      | 1.43 sec                                                                   | 1.46 sec: 1.02x slower                                                               |
| deepcopy_reduce          | 2.18 us                                                                    | 2.24 us: 1.03x slower                                                                |
| xml_etree_parse          | 91.2 ms                                                                    | 93.9 ms: 1.03x slower                                                                |
| nqueens                  | 62.8 ms                                                                    | 64.7 ms: 1.03x slower                                                                |
| xml_etree_generate       | 55.9 ms                                                                    | 57.7 ms: 1.03x slower                                                                |
| tomli_loads              | 1.59 sec                                                                   | 1.65 sec: 1.04x slower                                                               |
| pycparser                | 738 ms                                                                     | 780 ms: 1.06x slower                                                                 |
| telco                    | 4.72 ms                                                                    | 5.05 ms: 1.07x slower                                                                |
| Geometric mean           | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (27): regex_v8, unpickle, async_tree_memoization, python_startup_no_site, gc_traversal, async_tree_cpu_io_mixed, pathlib, scimark_monte_carlo, docutils, pickle_dict, chaos, meteor_contest, scimark_fft, sqlglot_normalize, richards, deltablue, scimark_sparse_mat_mult, comprehensions, bench_mp_pool, float, asyncio_tcp, async_tree_io, async_tree_none, create_gc_cycles, python_startup, mako, bench_thread_pool


# HPT report

- Reliability score: 51.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
