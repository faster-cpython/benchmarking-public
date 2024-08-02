# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: darwin-arm64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.11x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.74x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 181 ms: 1.06x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.96 ms: 1.26x faster                                                  |
| docutils       | 1.73 sec                                               | 1.66 sec: 1.04x faster                                                 |
| html5lib       | 42.4 ms                                                | 33.3 ms: 1.27x faster                                                  |
| tornado_http   | 86.7 ms                                                | 69.5 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 219 ms: 1.78x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 268 ms: 1.76x faster                                                   |
| async_tree_io           | 980 ms                                                 | 566 ms: 1.73x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 477 ms: 1.36x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.65x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 77.4 ms: 1.20x faster                                                  |
| float          | 69.0 ms                                                | 60.5 ms: 1.14x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| regex_compile  | 95.3 ms                                                | 95.8 ms: 1.01x slower                                                  |
| regex_v8       | 17.1 ms                                                | 17.6 ms: 1.03x slower                                                  |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 225 us: 1.25x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.56 ms: 1.24x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 41.0 ms: 1.13x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 175 us: 1.11x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.62 sec: 1.05x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| unpickle             | 8.80 us                                                | 9.26 us: 1.05x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 76.4 ms: 1.06x slower                                                  |
| pickle               | 6.97 us                                                | 7.51 us: 1.08x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.97 us: 1.08x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.93 us: 1.09x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 58.8 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.5 ms: 1.33x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 11.5 ms: 1.46x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 8.85 ms: 1.11x faster                                                  |
| django_template | 26.4 ms                                                | 23.7 ms: 1.11x faster                                                  |
| genshi_text     | 17.3 ms                                                | 17.3 ms: 1.00x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 35.8 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 106 us: 3.05x faster                                                   |
| async_tree_none          | 388 ms                                                 | 219 ms: 1.78x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 268 ms: 1.76x faster                                                   |
| async_tree_io            | 980 ms                                                 | 566 ms: 1.73x faster                                                   |
| raytrace                 | 301 ms                                                 | 180 ms: 1.67x faster                                                   |
| deltablue                | 4.91 ms                                                | 2.95 ms: 1.66x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 438 ms: 1.50x faster                                                   |
| pylint                   | 277 ms                                                 | 191 ms: 1.45x faster                                                   |
| richards_super           | 57.8 ms                                                | 40.6 ms: 1.42x faster                                                  |
| chaos                    | 65.8 ms                                                | 46.3 ms: 1.42x faster                                                  |
| mypy2                    | 607 ms                                                 | 429 ms: 1.42x faster                                                   |
| logging_simple           | 4.45 us                                                | 3.17 us: 1.40x faster                                                  |
| logging_format           | 4.83 us                                                | 3.45 us: 1.40x faster                                                  |
| generators               | 32.3 ms                                                | 23.5 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 477 ms: 1.36x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 947 us: 1.31x faster                                                   |
| richards                 | 48.7 ms                                                | 37.2 ms: 1.31x faster                                                  |
| thrift                   | 572 us                                                 | 442 us: 1.30x faster                                                   |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.24 sec: 1.29x faster                                                 |
| go                       | 151 ms                                                 | 117 ms: 1.28x faster                                                   |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                                  |
| html5lib                 | 42.4 ms                                                | 33.3 ms: 1.27x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.96 ms: 1.26x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.14 ms: 1.26x faster                                                  |
| tornado_http             | 86.7 ms                                                | 69.5 ms: 1.25x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 225 us: 1.25x faster                                                   |
| json_dumps               | 8.11 ms                                                | 6.56 ms: 1.24x faster                                                  |
| logging_silent           | 117 ns                                                 | 95.1 ns: 1.23x faster                                                  |
| pycparser                | 877 ms                                                 | 727 ms: 1.21x faster                                                   |
| nbody                    | 93.0 ms                                                | 77.4 ms: 1.20x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 29.5 ms: 1.20x faster                                                  |
| scimark_sor              | 128 ms                                                 | 107 ms: 1.19x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 61.0 ms: 1.18x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| gunicorn                 | 1.30 ms                                                | 1.12 ms: 1.16x faster                                                  |
| aiohttp                  | 1.22 ms                                                | 1.05 ms: 1.16x faster                                                  |
| float                    | 69.0 ms                                                | 60.5 ms: 1.14x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 41.0 ms: 1.13x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 571 ms: 1.12x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 1.17 sec: 1.12x faster                                                 |
| dask                     | 253 ms                                                 | 227 ms: 1.12x faster                                                   |
| mako                     | 9.87 ms                                                | 8.85 ms: 1.11x faster                                                  |
| django_template          | 26.4 ms                                                | 23.7 ms: 1.11x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 175 us: 1.11x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 2.10 us: 1.11x faster                                                  |
| deepcopy                 | 272 us                                                 | 251 us: 1.08x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 60.5 ms: 1.08x faster                                                  |
| pyflate                  | 427 ms                                                 | 396 ms: 1.08x faster                                                   |
| pathlib                  | 24.5 ms                                                | 22.8 ms: 1.07x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 85.9 ms: 1.07x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 32.6 us: 1.07x faster                                                  |
| scimark_lu               | 103 ms                                                 | 97.0 ms: 1.06x faster                                                  |
| 2to3                     | 192 ms                                                 | 181 ms: 1.06x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.62 sec: 1.05x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.55 sec: 1.05x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 12.6 ms: 1.05x faster                                                  |
| hexiom                   | 6.19 ms                                                | 5.94 ms: 1.04x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.66 sec: 1.04x faster                                                 |
| json                     | 3.08 ms                                                | 3.01 ms: 1.02x faster                                                  |
| sympy_expand             | 269 ms                                                 | 264 ms: 1.02x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 93.4 ms: 1.02x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 521 us: 1.01x faster                                                   |
| sympy_str                | 165 ms                                                 | 163 ms: 1.01x faster                                                   |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| scimark_fft              | 224 ms                                                 | 223 ms: 1.01x faster                                                   |
| genshi_text              | 17.3 ms                                                | 17.3 ms: 1.00x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                   |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| regex_compile            | 95.3 ms                                                | 95.8 ms: 1.01x slower                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 37.2 ms: 1.01x slower                                                  |
| meteor_contest           | 77.7 ms                                                | 78.8 ms: 1.01x slower                                                  |
| comprehensions           | 16.9 us                                                | 17.3 us: 1.02x slower                                                  |
| regex_v8                 | 17.1 ms                                                | 17.6 ms: 1.03x slower                                                  |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| fannkuch                 | 303 ms                                                 | 312 ms: 1.03x slower                                                   |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.05x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.26 us: 1.05x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 35.8 ms: 1.06x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 76.4 ms: 1.06x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 913 us: 1.06x slower                                                   |
| nqueens                  | 63.8 ms                                                | 68.0 ms: 1.07x slower                                                  |
| pickle                   | 6.97 us                                                | 7.51 us: 1.08x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.97 us: 1.08x slower                                                  |
| unpickle_list            | 2.69 us                                                | 2.93 us: 1.09x slower                                                  |
| coverage                 | 41.5 ms                                                | 45.3 ms: 1.09x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 58.8 ms: 1.10x slower                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.77 ms: 1.10x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.62 us: 1.11x slower                                                  |
| flaskblogging            | 2.65 ms                                                | 3.26 ms: 1.23x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 47.8 ms: 1.28x slower                                                  |
| async_generators         | 231 ms                                                 | 297 ms: 1.28x slower                                                   |
| python_startup           | 10.9 ms                                                | 14.5 ms: 1.33x slower                                                  |
| telco                    | 3.49 ms                                                | 4.95 ms: 1.42x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 11.5 ms: 1.46x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.11x faster                                                           |
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (12) of results/bm-20240604-3.13.0b1+-6725c78-PYTHON_UOPS/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.74x