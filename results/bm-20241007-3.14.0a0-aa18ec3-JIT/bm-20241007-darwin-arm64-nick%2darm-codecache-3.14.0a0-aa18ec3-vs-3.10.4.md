# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 0.68x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 169 ms: 1.13x faster                                           |
| docutils       | 1.73 sec                                               | 1.49 sec: 1.17x faster                                         |
| html5lib       | 42.4 ms                                                | 32.6 ms: 1.30x faster                                          |
| tornado_http   | 86.7 ms                                                | 73.4 ms: 1.18x faster                                          |
| Geometric mean | (ref)                                                  | 1.19x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 200 ms: 1.94x faster                                           |
| async_tree_memoization  | 474 ms                                                 | 250 ms: 1.89x faster                                           |
| async_tree_io           | 980 ms                                                 | 587 ms: 1.67x faster                                           |
| async_tree_cpu_io_mixed | 649 ms                                                 | 460 ms: 1.41x faster                                           |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.3 ms: 1.49x faster                                          |
| nbody          | 93.0 ms                                                | 63.5 ms: 1.46x faster                                          |
| Geometric mean | (ref)                                                  | 1.30x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 71.6 ms: 1.33x faster                                          |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                           |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                          |
| regex_effbot   | 2.46 ms                                                | 2.64 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 175 us: 1.61x faster                                           |
| unpickle_pure_python | 194 us                                                 | 130 us: 1.50x faster                                           |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.38x faster                                         |
| xml_etree_process    | 46.5 ms                                                | 33.7 ms: 1.38x faster                                          |
| json_dumps           | 8.11 ms                                                | 6.10 ms: 1.33x faster                                          |
| xml_etree_generate   | 53.5 ms                                                | 49.1 ms: 1.09x faster                                          |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                           |
| json_loads           | 16.4 us                                                | 16.3 us: 1.01x faster                                          |
| xml_etree_iterparse  | 72.1 ms                                                | 71.5 ms: 1.01x faster                                          |
| unpickle             | 8.80 us                                                | 9.07 us: 1.03x slower                                          |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.06x slower                                          |
| pickle               | 6.97 us                                                | 7.44 us: 1.07x slower                                          |
| pickle_list          | 2.74 us                                                | 2.94 us: 1.07x slower                                          |
| unpickle_list        | 2.69 us                                                | 3.02 us: 1.12x slower                                          |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.1 ms: 1.48x slower                                          |
| python_startup_no_site | 7.91 ms                                                | 13.3 ms: 1.69x slower                                          |
| Geometric mean         | (ref)                                                  | 1.58x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.37 ms: 1.55x faster                                          |
| django_template | 26.4 ms                                                | 20.2 ms: 1.31x faster                                          |
| genshi_text     | 17.3 ms                                                | 14.6 ms: 1.19x faster                                          |
| genshi_xml      | 33.8 ms                                                | 32.1 ms: 1.05x faster                                          |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.5 us: 3.42x faster                                          |
| deepcopy_memo            | 34.7 us                                                | 16.3 us: 2.13x faster                                          |
| deltablue                | 4.91 ms                                                | 2.36 ms: 2.08x faster                                          |
| async_tree_none          | 388 ms                                                 | 200 ms: 1.94x faster                                           |
| logging_silent           | 117 ns                                                 | 60.7 ns: 1.93x faster                                          |
| async_tree_memoization   | 474 ms                                                 | 250 ms: 1.89x faster                                           |
| deepcopy                 | 272 us                                                 | 148 us: 1.84x faster                                           |
| raytrace                 | 301 ms                                                 | 171 ms: 1.76x faster                                           |
| richards_super           | 57.8 ms                                                | 34.0 ms: 1.70x faster                                          |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                           |
| async_tree_io            | 980 ms                                                 | 587 ms: 1.67x faster                                           |
| chaos                    | 65.8 ms                                                | 39.7 ms: 1.66x faster                                          |
| go                       | 151 ms                                                 | 93.4 ms: 1.61x faster                                          |
| pickle_pure_python       | 281 us                                                 | 175 us: 1.61x faster                                           |
| scimark_lu               | 103 ms                                                 | 64.2 ms: 1.60x faster                                          |
| richards                 | 48.7 ms                                                | 30.6 ms: 1.59x faster                                          |
| mako                     | 9.87 ms                                                | 6.37 ms: 1.55x faster                                          |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.55x faster                                          |
| sqlglot_parse            | 1.24 ms                                                | 804 us: 1.55x faster                                           |
| unpickle_pure_python     | 194 us                                                 | 130 us: 1.50x faster                                           |
| asyncio_tcp              | 659 ms                                                 | 442 ms: 1.49x faster                                           |
| float                    | 69.0 ms                                                | 46.3 ms: 1.49x faster                                          |
| scimark_sor              | 128 ms                                                 | 87.0 ms: 1.47x faster                                          |
| sqlglot_transpile        | 1.44 ms                                                | 980 us: 1.47x faster                                           |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.46x faster                                          |
| logging_simple           | 4.45 us                                                | 3.04 us: 1.46x faster                                          |
| logging_format           | 4.83 us                                                | 3.31 us: 1.46x faster                                          |
| scimark_monte_carlo      | 65.6 ms                                                | 46.1 ms: 1.42x faster                                          |
| pylint                   | 277 ms                                                 | 195 ms: 1.42x faster                                           |
| spectral_norm            | 94.8 ms                                                | 66.9 ms: 1.42x faster                                          |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 460 ms: 1.41x faster                                           |
| hexiom                   | 6.19 ms                                                | 4.42 ms: 1.40x faster                                          |
| crypto_pyaes             | 71.8 ms                                                | 51.8 ms: 1.39x faster                                          |
| pprint_safe_repr         | 641 ms                                                 | 462 ms: 1.39x faster                                           |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.38x faster                                         |
| thrift                   | 572 us                                                 | 415 us: 1.38x faster                                           |
| xml_etree_process        | 46.5 ms                                                | 33.7 ms: 1.38x faster                                          |
| comprehensions           | 16.9 us                                                | 12.5 us: 1.36x faster                                          |
| pycparser                | 877 ms                                                 | 649 ms: 1.35x faster                                           |
| pyflate                  | 427 ms                                                 | 317 ms: 1.35x faster                                           |
| generators               | 32.3 ms                                                | 24.1 ms: 1.34x faster                                          |
| pprint_pformat           | 1.30 sec                                               | 979 ms: 1.33x faster                                           |
| regex_compile            | 95.3 ms                                                | 71.6 ms: 1.33x faster                                          |
| json_dumps               | 8.11 ms                                                | 6.10 ms: 1.33x faster                                          |
| django_template          | 26.4 ms                                                | 20.2 ms: 1.31x faster                                          |
| html5lib                 | 42.4 ms                                                | 32.6 ms: 1.30x faster                                          |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                          |
| sympy_sum                | 92.2 ms                                                | 74.0 ms: 1.25x faster                                          |
| dulwich_log              | 35.3 ms                                                | 28.5 ms: 1.24x faster                                          |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                         |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                           |
| genshi_text              | 17.3 ms                                                | 14.6 ms: 1.19x faster                                          |
| tornado_http             | 86.7 ms                                                | 73.4 ms: 1.18x faster                                          |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                           |
| sympy_str                | 165 ms                                                 | 141 ms: 1.17x faster                                           |
| docutils                 | 1.73 sec                                               | 1.49 sec: 1.17x faster                                         |
| fannkuch                 | 303 ms                                                 | 260 ms: 1.16x faster                                           |
| sympy_expand             | 269 ms                                                 | 235 ms: 1.14x faster                                           |
| 2to3                     | 192 ms                                                 | 169 ms: 1.13x faster                                           |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.03 ms: 1.13x faster                                          |
| pathlib                  | 24.5 ms                                                | 21.8 ms: 1.12x faster                                          |
| sympy_integrate          | 13.1 ms                                                | 11.7 ms: 1.12x faster                                          |
| nqueens                  | 63.8 ms                                                | 57.3 ms: 1.11x faster                                          |
| mdp                      | 1.63 sec                                               | 1.47 sec: 1.11x faster                                         |
| bench_thread_pool        | 527 us                                                 | 478 us: 1.10x faster                                           |
| sqlglot_normalize        | 190 ms                                                 | 174 ms: 1.09x faster                                           |
| xml_etree_generate       | 53.5 ms                                                | 49.1 ms: 1.09x faster                                          |
| sqlglot_optimize         | 36.8 ms                                                | 33.8 ms: 1.09x faster                                          |
| json                     | 3.08 ms                                                | 2.84 ms: 1.09x faster                                          |
| meteor_contest           | 77.7 ms                                                | 73.5 ms: 1.06x faster                                          |
| genshi_xml               | 33.8 ms                                                | 32.1 ms: 1.05x faster                                          |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                          |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                           |
| json_loads               | 16.4 us                                                | 16.3 us: 1.01x faster                                          |
| xml_etree_iterparse      | 72.1 ms                                                | 71.5 ms: 1.01x faster                                          |
| unpickle                 | 8.80 us                                                | 9.07 us: 1.03x slower                                          |
| create_gc_cycles         | 860 us                                                 | 899 us: 1.05x slower                                           |
| gc_traversal             | 2.36 ms                                                | 2.48 ms: 1.05x slower                                          |
| sqlite_synth             | 1.46 us                                                | 1.53 us: 1.05x slower                                          |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.06x slower                                          |
| pickle                   | 6.97 us                                                | 7.44 us: 1.07x slower                                          |
| regex_effbot             | 2.46 ms                                                | 2.64 ms: 1.07x slower                                          |
| pickle_list              | 2.74 us                                                | 2.94 us: 1.07x slower                                          |
| coverage                 | 41.5 ms                                                | 44.6 ms: 1.07x slower                                          |
| unpickle_list            | 2.69 us                                                | 3.02 us: 1.12x slower                                          |
| async_generators         | 231 ms                                                 | 289 ms: 1.25x slower                                           |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.31x slower                                          |
| bench_mp_pool            | 37.4 ms                                                | 50.8 ms: 1.36x slower                                          |
| python_startup           | 10.9 ms                                                | 16.1 ms: 1.48x slower                                          |
| python_startup_no_site   | 7.91 ms                                                | 13.3 ms: 1.69x slower                                          |
| unpack_sequence          | 39.0 ns                                                | 74.9 ns: 1.92x slower                                          |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                   |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-darwin-arm64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 0.68x