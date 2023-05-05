
# Results vs. base

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: darwin-arm64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 173 ms                                                                 | 174 ms: 1.00x slower                                                              |
| docutils       | 1.56 sec                                                               | 1.57 sec: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 281 ms                                                                 | 281 ms: 1.00x slower                                                              |
| nbody          | 69.7 ms                                                                | 70.3 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 78.7 ms                                                                | 78.6 ms: 1.00x faster                                                             |
| regex_v8       | 16.3 ms                                                                | 16.3 ms: 1.00x faster                                                             |
| regex_effbot   | 2.69 ms                                                                | 2.78 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 194 us                                                                 | 193 us: 1.01x faster                                                              |
| unpickle_pure_python | 151 us                                                                 | 150 us: 1.00x faster                                                              |
| xml_etree_generate   | 58.0 ms                                                                | 58.2 ms: 1.00x slower                                                             |
| pickle_dict          | 19.0 us                                                                | 19.0 us: 1.00x slower                                                             |
| xml_etree_process    | 40.2 ms                                                                | 40.4 ms: 1.00x slower                                                             |
| unpickle_list        | 3.19 us                                                                | 3.21 us: 1.01x slower                                                             |
| pickle               | 7.95 us                                                                | 8.00 us: 1.01x slower                                                             |
| json_dumps           | 6.92 ms                                                                | 6.98 ms: 1.01x slower                                                             |
| pickle_list          | 3.05 us                                                                | 3.07 us: 1.01x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (4): unpickle, json_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 10.4 ms                                                                | 10.4 ms: 1.00x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 | bm-20230504-darwin-arm64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| logging_silent          | 71.0 ns                                                                | 69.5 ns: 1.02x faster                                                             |
| telco                   | 4.03 ms                                                                | 3.95 ms: 1.02x faster                                                             |
| fannkuch                | 279 ms                                                                 | 274 ms: 1.02x faster                                                              |
| richards                | 32.4 ms                                                                | 32.0 ms: 1.01x faster                                                             |
| sqlalchemy_imperative   | 7.37 ms                                                                | 7.29 ms: 1.01x faster                                                             |
| pprint_pformat          | 1.04 sec                                                               | 1.03 sec: 1.01x faster                                                            |
| pprint_safe_repr        | 511 ms                                                                 | 506 ms: 1.01x faster                                                              |
| pickle_pure_python      | 194 us                                                                 | 193 us: 1.01x faster                                                              |
| comprehensions          | 18.0 us                                                                | 17.8 us: 1.01x faster                                                             |
| sqlglot_normalize       | 200 ms                                                                 | 199 ms: 1.01x faster                                                              |
| chaos                   | 48.4 ms                                                                | 48.1 ms: 1.01x faster                                                             |
| sqlglot_transpile       | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                                             |
| logging_format          | 4.00 us                                                                | 3.99 us: 1.00x faster                                                             |
| unpickle_pure_python    | 151 us                                                                 | 150 us: 1.00x faster                                                              |
| scimark_sor             | 86.4 ms                                                                | 86.0 ms: 1.00x faster                                                             |
| deltablue               | 2.47 ms                                                                | 2.46 ms: 1.00x faster                                                             |
| logging_simple          | 3.72 us                                                                | 3.70 us: 1.00x faster                                                             |
| sqlglot_parse           | 903 us                                                                 | 900 us: 1.00x faster                                                              |
| scimark_fft             | 214 ms                                                                 | 213 ms: 1.00x faster                                                              |
| sqlite_synth            | 1.60 us                                                                | 1.59 us: 1.00x faster                                                             |
| hexiom                  | 4.32 ms                                                                | 4.31 ms: 1.00x faster                                                             |
| go                      | 109 ms                                                                 | 109 ms: 1.00x faster                                                              |
| pyflate                 | 343 ms                                                                 | 343 ms: 1.00x faster                                                              |
| dulwich_log             | 30.7 ms                                                                | 30.6 ms: 1.00x faster                                                             |
| regex_compile           | 78.7 ms                                                                | 78.6 ms: 1.00x faster                                                             |
| regex_v8                | 16.3 ms                                                                | 16.3 ms: 1.00x faster                                                             |
| pidigits                | 281 ms                                                                 | 281 ms: 1.00x slower                                                              |
| scimark_lu              | 82.0 ms                                                                | 82.1 ms: 1.00x slower                                                             |
| 2to3                    | 173 ms                                                                 | 174 ms: 1.00x slower                                                              |
| python_startup_no_site  | 10.4 ms                                                                | 10.4 ms: 1.00x slower                                                             |
| xml_etree_generate      | 58.0 ms                                                                | 58.2 ms: 1.00x slower                                                             |
| pickle_dict             | 19.0 us                                                                | 19.0 us: 1.00x slower                                                             |
| docutils                | 1.56 sec                                                               | 1.57 sec: 1.00x slower                                                            |
| coroutines              | 18.0 ms                                                                | 18.1 ms: 1.00x slower                                                             |
| xml_etree_process       | 40.2 ms                                                                | 40.4 ms: 1.00x slower                                                             |
| mdp                     | 1.58 sec                                                               | 1.59 sec: 1.00x slower                                                            |
| generators              | 24.9 ms                                                                | 25.0 ms: 1.00x slower                                                             |
| deepcopy_memo           | 26.4 us                                                                | 26.5 us: 1.01x slower                                                             |
| unpickle_list           | 3.19 us                                                                | 3.21 us: 1.01x slower                                                             |
| deepcopy_reduce         | 2.13 us                                                                | 2.14 us: 1.01x slower                                                             |
| scimark_sparse_mat_mult | 3.31 ms                                                                | 3.33 ms: 1.01x slower                                                             |
| coverage                | 58.8 ms                                                                | 59.1 ms: 1.01x slower                                                             |
| pickle                  | 7.95 us                                                                | 8.00 us: 1.01x slower                                                             |
| nqueens                 | 63.4 ms                                                                | 63.8 ms: 1.01x slower                                                             |
| async_generators        | 315 ms                                                                 | 318 ms: 1.01x slower                                                              |
| json_dumps              | 6.92 ms                                                                | 6.98 ms: 1.01x slower                                                             |
| pickle_list             | 3.05 us                                                                | 3.07 us: 1.01x slower                                                             |
| deepcopy                | 239 us                                                                 | 241 us: 1.01x slower                                                              |
| nbody                   | 69.7 ms                                                                | 70.3 ms: 1.01x slower                                                             |
| regex_effbot            | 2.69 ms                                                                | 2.78 ms: 1.03x slower                                                             |
| asyncio_tcp             | 420 ms                                                                 | 451 ms: 1.07x slower                                                              |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (30): tornado_http, json, unpickle, pycparser, async_tree_memoization, meteor_contest, dask, unpack_sequence, float, crypto_pyaes, async_tree_cpu_io_mixed, gc_traversal, json_loads, sqlalchemy_declarative, sqlglot_optimize, async_tree_none, xml_etree_iterparse, raytrace, regex_dna, mypy2, spectral_norm, bench_thread_pool, create_gc_cycles, mako, xml_etree_parse, pathlib, python_startup, async_tree_io, scimark_monte_carlo, bench_mp_pool
