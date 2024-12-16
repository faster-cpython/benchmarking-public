# Results vs. 3.10.4

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: darwin-arm64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.250x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 170 ms: 1.13x faster                                                   |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                 |
| html5lib       | 42.4 ms                                                | 33.4 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 378 ms: 2.59x faster                                                   |
| async_tree_none         | 388 ms                                                 | 168 ms: 2.32x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 205 ms: 2.32x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 422 ms: 1.54x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.15x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.7 ms: 1.46x faster                                                  |
| float          | 69.0 ms                                                | 47.8 ms: 1.44x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 69.5 ms: 1.37x faster                                                  |
| regex_dna      | 174 ms                                                 | 136 ms: 1.28x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.01 ms: 1.22x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                 | 125 us: 1.56x faster                                                   |
| pickle_pure_python   | 281 us                                                 | 197 us: 1.42x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.21 sec: 1.41x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 35.1 ms: 1.33x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.16 ms: 1.13x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 49.3 ms: 1.09x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 69.9 ms: 1.03x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 21.6 ms: 1.98x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 16.6 ms: 2.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 2.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.26 ms: 1.58x faster                                                  |
| django_template | 26.4 ms                                                | 23.2 ms: 1.14x faster                                                  |
| genshi_text     | 17.3 ms                                                | 17.6 ms: 1.02x slower                                                  |
| genshi_xml      | 33.8 ms                                                | 41.6 ms: 1.23x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 99.5 us: 3.25x faster                                                  |
| async_tree_io            | 980 ms                                                 | 378 ms: 2.59x faster                                                   |
| async_tree_none          | 388 ms                                                 | 168 ms: 2.32x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 205 ms: 2.32x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 17.2 us: 2.02x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.55 ms: 1.93x faster                                                  |
| deepcopy                 | 272 us                                                 | 158 us: 1.71x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                   |
| pylint                   | 277 ms                                                 | 166 ms: 1.67x faster                                                   |
| raytrace                 | 301 ms                                                 | 184 ms: 1.64x faster                                                   |
| mako                     | 9.87 ms                                                | 6.26 ms: 1.58x faster                                                  |
| scimark_sor              | 128 ms                                                 | 82.2 ms: 1.56x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 125 us: 1.56x faster                                                   |
| chaos                    | 65.8 ms                                                | 42.4 ms: 1.55x faster                                                  |
| logging_silent           | 117 ns                                                 | 75.7 ns: 1.55x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 422 ms: 1.54x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 62.0 ms: 1.53x faster                                                  |
| go                       | 151 ms                                                 | 99.7 ms: 1.51x faster                                                  |
| richards_super           | 57.8 ms                                                | 38.4 ms: 1.51x faster                                                  |
| scimark_lu               | 103 ms                                                 | 68.6 ms: 1.50x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.8 ms: 1.46x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.59 us: 1.46x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.7 ms: 1.46x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 854 us: 1.46x faster                                                   |
| float                    | 69.0 ms                                                | 47.8 ms: 1.44x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 197 us: 1.42x faster                                                   |
| richards                 | 48.7 ms                                                | 34.6 ms: 1.41x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.21 sec: 1.41x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.03 ms: 1.40x faster                                                  |
| regex_compile            | 95.3 ms                                                | 69.5 ms: 1.37x faster                                                  |
| pyflate                  | 427 ms                                                 | 319 ms: 1.34x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 53.8 ms: 1.34x faster                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.64 ms: 1.34x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 35.1 ms: 1.33x faster                                                  |
| scimark_fft              | 224 ms                                                 | 172 ms: 1.31x faster                                                   |
| logging_simple           | 4.45 us                                                | 3.43 us: 1.30x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.01 sec: 1.30x faster                                                 |
| logging_format           | 4.83 us                                                | 3.73 us: 1.29x faster                                                  |
| thrift                   | 572 us                                                 | 443 us: 1.29x faster                                                   |
| pycparser                | 877 ms                                                 | 680 ms: 1.29x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 498 ms: 1.29x faster                                                   |
| regex_dna                | 174 ms                                                 | 136 ms: 1.28x faster                                                   |
| html5lib                 | 42.4 ms                                                | 33.4 ms: 1.27x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.91 ms: 1.26x faster                                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 58.9 ms: 1.24x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 75.4 ms: 1.22x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.01 ms: 1.22x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                                  |
| comprehensions           | 16.9 us                                                | 14.0 us: 1.21x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.89 ms: 1.18x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.5 ms: 1.18x faster                                                  |
| mypy2                    | 607 ms                                                 | 526 ms: 1.15x faster                                                   |
| sympy_str                | 165 ms                                                 | 144 ms: 1.15x faster                                                   |
| django_template          | 26.4 ms                                                | 23.2 ms: 1.14x faster                                                  |
| generators               | 32.3 ms                                                | 28.4 ms: 1.14x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.16 ms: 1.13x faster                                                  |
| 2to3                     | 192 ms                                                 | 170 ms: 1.13x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 11.8 ms: 1.12x faster                                                  |
| fannkuch                 | 303 ms                                                 | 272 ms: 1.11x faster                                                   |
| sympy_expand             | 269 ms                                                 | 244 ms: 1.10x faster                                                   |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.10x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 49.3 ms: 1.09x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 34.2 ms: 1.08x faster                                                  |
| json                     | 3.08 ms                                                | 2.88 ms: 1.07x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.7 ms: 1.07x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 503 us: 1.05x faster                                                   |
| mdp                      | 1.63 sec                                               | 1.57 sec: 1.04x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 69.9 ms: 1.03x faster                                                  |
| nqueens                  | 63.8 ms                                                | 62.7 ms: 1.02x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 187 ms: 1.02x faster                                                   |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| genshi_text              | 17.3 ms                                                | 17.6 ms: 1.02x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.06x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.2 ms: 1.07x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 41.6 ms: 1.23x slower                                                  |
| telco                    | 3.49 ms                                                | 4.46 ms: 1.28x slower                                                  |
| async_generators         | 231 ms                                                 | 300 ms: 1.30x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 3.07 ms: 1.30x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 1.28 ms: 1.49x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 63.3 ms: 1.69x slower                                                  |
| python_startup           | 10.9 ms                                                | 21.6 ms: 1.98x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 16.6 ms: 2.09x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-darwin-arm64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.250x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.37x