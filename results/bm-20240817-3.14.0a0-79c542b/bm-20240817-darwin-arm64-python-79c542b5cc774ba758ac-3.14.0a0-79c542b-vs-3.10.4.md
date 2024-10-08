# Results vs. 3.10.4

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 162 ms: 1.19x faster                                                  |
| docutils       | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                |
| html5lib       | 42.4 ms                                                | 31.4 ms: 1.35x faster                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 192 ms: 2.03x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 241 ms: 1.97x faster                                                  |
| async_tree_io           | 980 ms                                                 | 539 ms: 1.82x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.8 ms: 1.53x faster                                                 |
| float          | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.0 ms: 1.40x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.38 ms: 1.27x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.3 ms: 1.25x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.8 ms: 1.04x slower                                                 |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 13.8 ms: 1.27x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 10.9 ms: 1.38x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.32x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.96 ms: 1.42x faster                                                 |
| django_template | 26.4 ms                                                | 19.6 ms: 1.34x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.1 ms: 1.23x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.4 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.2 us: 3.47x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.11 ms: 2.32x faster                                                 |
| raytrace                 | 301 ms                                                 | 147 ms: 2.04x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 17.1 us: 2.03x faster                                                 |
| async_tree_none          | 388 ms                                                 | 192 ms: 2.03x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 241 ms: 1.97x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.4 ns: 1.94x faster                                                 |
| deepcopy                 | 272 us                                                 | 146 us: 1.86x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.8 ms: 1.84x faster                                                 |
| async_tree_io            | 980 ms                                                 | 539 ms: 1.82x faster                                                  |
| richards_super           | 57.8 ms                                                | 33.3 ms: 1.73x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.0 us: 1.69x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 744 us: 1.67x faster                                                  |
| richards                 | 48.7 ms                                                | 30.3 ms: 1.61x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 902 us: 1.60x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 413 ms: 1.59x faster                                                  |
| generators               | 32.3 ms                                                | 20.3 ms: 1.59x faster                                                 |
| go                       | 151 ms                                                 | 96.6 ms: 1.56x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                                  |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                                  |
| nbody                    | 93.0 ms                                                | 60.8 ms: 1.53x faster                                                 |
| scimark_lu               | 103 ms                                                 | 67.8 ms: 1.52x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.10 ms: 1.51x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.5 ms: 1.51x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.07 us: 1.45x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| logging_format           | 4.83 us                                                | 3.40 us: 1.42x faster                                                 |
| mako                     | 9.87 ms                                                | 6.96 ms: 1.42x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.7 ms: 1.42x faster                                                 |
| float                    | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.2 ms: 1.41x faster                                                 |
| regex_compile            | 95.3 ms                                                | 68.0 ms: 1.40x faster                                                 |
| pycparser                | 877 ms                                                 | 638 ms: 1.37x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 466 ms: 1.37x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 952 ms: 1.37x faster                                                  |
| scimark_sor              | 128 ms                                                 | 93.8 ms: 1.37x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.4 ms: 1.35x faster                                                 |
| django_template          | 26.4 ms                                                | 19.6 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                  |
| thrift                   | 572 us                                                 | 432 us: 1.33x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 26.9 ms: 1.31x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 70.4 ms: 1.31x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.38 ms: 1.27x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.5 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 37.3 ms: 1.25x faster                                                 |
| sympy_str                | 165 ms                                                 | 134 ms: 1.24x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.1 ms: 1.23x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.81 ms: 1.22x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.3 ms: 1.20x faster                                                 |
| 2to3                     | 192 ms                                                 | 162 ms: 1.19x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.3 ms: 1.18x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 450 us: 1.17x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| fannkuch                 | 303 ms                                                 | 265 ms: 1.14x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 168 ms: 1.13x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.4 ms: 1.11x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.9 ms: 1.08x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.54 sec: 1.06x faster                                                |
| pathlib                  | 24.5 ms                                                | 23.4 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.98 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                 |
| regex_effbot             | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.8 ms: 1.04x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 895 us: 1.04x slower                                                  |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.4 ms: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 282 ms: 1.22x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 46.5 ms: 1.24x slower                                                 |
| python_startup           | 10.9 ms                                                | 13.8 ms: 1.27x slower                                                 |
| telco                    | 3.49 ms                                                | 4.58 ms: 1.31x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 10.9 ms: 1.38x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                          |

Benchmark hidden because not significant (3): tornado_http, asyncio_websockets, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240817-3.14.0a0-79c542b/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.67x