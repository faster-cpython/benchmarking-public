# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel
- machine: darwin-arm64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 172 ms: 1.11x faster                                                  |
| docutils       | 1.73 sec                                               | 1.51 sec: 1.14x faster                                                |
| html5lib       | 42.4 ms                                                | 31.1 ms: 1.36x faster                                                 |
| tornado_http   | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 232 ms: 2.04x faster                                                  |
| async_tree_none         | 388 ms                                                 | 194 ms: 2.01x faster                                                  |
| async_tree_io           | 980 ms                                                 | 516 ms: 1.90x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 47.4 ms: 1.45x faster                                                 |
| nbody          | 93.0 ms                                                | 64.1 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.9 ms: 1.31x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.00x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.57 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 174 us: 1.61x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.48x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.28 sec: 1.34x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 36.6 ms: 1.27x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.41 ms: 1.26x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 70.7 ms: 1.02x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 52.5 ms: 1.02x faster                                                 |
| json_loads           | 16.4 us                                                | 17.4 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.4 ms: 1.41x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.7 ms: 1.61x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.53 ms: 1.51x faster                                                 |
| django_template | 26.4 ms                                                | 22.2 ms: 1.19x faster                                                 |
| genshi_text     | 17.3 ms                                                | 15.9 ms: 1.09x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 40.3 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.9 us: 3.37x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.32 ms: 2.12x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.06x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 232 ms: 2.04x faster                                                  |
| async_tree_none          | 388 ms                                                 | 194 ms: 2.01x faster                                                  |
| async_tree_io            | 980 ms                                                 | 516 ms: 1.90x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.9 ns: 1.89x faster                                                 |
| raytrace                 | 301 ms                                                 | 164 ms: 1.83x faster                                                  |
| deepcopy                 | 272 us                                                 | 152 us: 1.79x faster                                                  |
| richards_super           | 57.8 ms                                                | 34.6 ms: 1.67x faster                                                 |
| chaos                    | 65.8 ms                                                | 39.4 ms: 1.67x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 174 us: 1.61x faster                                                  |
| richards                 | 48.7 ms                                                | 30.7 ms: 1.59x faster                                                 |
| pylint                   | 277 ms                                                 | 180 ms: 1.54x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 430 ms: 1.53x faster                                                  |
| mako                     | 9.87 ms                                                | 6.53 ms: 1.51x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.54 us: 1.51x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 827 us: 1.50x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.9 ms: 1.49x faster                                                 |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.48x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.03 us: 1.47x faster                                                 |
| float                    | 69.0 ms                                                | 47.4 ms: 1.45x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 994 us: 1.45x faster                                                  |
| nbody                    | 93.0 ms                                                | 64.1 ms: 1.45x faster                                                 |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.40 ms: 1.41x faster                                                 |
| generators               | 32.3 ms                                                | 23.2 ms: 1.40x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 51.9 ms: 1.38x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 68.6 ms: 1.38x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.38x faster                                                 |
| html5lib                 | 42.4 ms                                                | 31.1 ms: 1.36x faster                                                 |
| pyflate                  | 427 ms                                                 | 318 ms: 1.34x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.28 sec: 1.34x faster                                                |
| thrift                   | 572 us                                                 | 435 us: 1.31x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 488 ms: 1.31x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 998 ms: 1.31x faster                                                  |
| regex_compile            | 95.3 ms                                                | 72.9 ms: 1.31x faster                                                 |
| pycparser                | 877 ms                                                 | 674 ms: 1.30x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                 |
| tornado_http             | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 36.6 ms: 1.27x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.41 ms: 1.26x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 73.0 ms: 1.26x faster                                                 |
| scimark_sor              | 128 ms                                                 | 102 ms: 1.25x faster                                                  |
| scimark_lu               | 103 ms                                                 | 82.6 ms: 1.25x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.23x faster                                                |
| fannkuch                 | 303 ms                                                 | 248 ms: 1.22x faster                                                  |
| sympy_str                | 165 ms                                                 | 138 ms: 1.20x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.0 ms: 1.20x faster                                                 |
| django_template          | 26.4 ms                                                | 22.2 ms: 1.19x faster                                                 |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.18x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.51 sec: 1.14x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.02 ms: 1.13x faster                                                 |
| dask                     | 253 ms                                                 | 225 ms: 1.13x faster                                                  |
| sympy_expand             | 269 ms                                                 | 240 ms: 1.12x faster                                                  |
| 2to3                     | 192 ms                                                 | 172 ms: 1.11x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 33.1 ms: 1.11x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 475 us: 1.11x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.47 sec: 1.11x faster                                                |
| nqueens                  | 63.8 ms                                                | 57.6 ms: 1.11x faster                                                 |
| genshi_text              | 17.3 ms                                                | 15.9 ms: 1.09x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.7 ms: 1.07x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 178 ms: 1.07x faster                                                  |
| json                     | 3.08 ms                                                | 2.96 ms: 1.04x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 70.7 ms: 1.02x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 52.5 ms: 1.02x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.00x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.57 ms: 1.05x slower                                                 |
| json_loads               | 16.4 us                                                | 17.4 us: 1.06x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 913 us: 1.06x slower                                                  |
| coverage                 | 41.5 ms                                                | 46.2 ms: 1.11x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 40.3 ms: 1.19x slower                                                 |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                                  |
| telco                    | 3.49 ms                                                | 4.61 ms: 1.32x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 50.3 ms: 1.34x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.4 ms: 1.41x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.7 ms: 1.61x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, asyncio_websockets, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.30x