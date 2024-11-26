# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.227x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.42x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 184 ms: 1.04x faster                                                   |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                 |
| html5lib       | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 201 ms: 1.93x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 245 ms: 1.93x faster                                                   |
| async_tree_io           | 980 ms                                                 | 582 ms: 1.68x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 459 ms: 1.41x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                  |
| nbody          | 93.0 ms                                                | 65.9 ms: 1.41x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 75.3 ms: 1.27x faster                                                  |
| regex_dna      | 174 ms                                                 | 143 ms: 1.22x faster                                                   |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.48 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 134 us: 1.45x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.36x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 34.8 ms: 1.33x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.13 ms: 1.14x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 49.6 ms: 1.08x faster                                                  |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.8 ms: 1.73x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 14.4 ms: 1.83x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.78x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.44 ms: 1.53x faster                                                  |
| django_template | 26.4 ms                                                | 22.9 ms: 1.15x faster                                                  |
| genshi_text     | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 42.4 ms: 1.25x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 98.5 us: 3.28x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.41 ms: 2.04x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 17.1 us: 2.03x faster                                                  |
| async_tree_none          | 388 ms                                                 | 201 ms: 1.93x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 245 ms: 1.93x faster                                                   |
| deepcopy                 | 272 us                                                 | 155 us: 1.75x faster                                                   |
| raytrace                 | 301 ms                                                 | 173 ms: 1.74x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                   |
| async_tree_io            | 980 ms                                                 | 582 ms: 1.68x faster                                                   |
| logging_silent           | 117 ns                                                 | 70.9 ns: 1.65x faster                                                  |
| chaos                    | 65.8 ms                                                | 41.9 ms: 1.57x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                                   |
| scimark_lu               | 103 ms                                                 | 65.8 ms: 1.56x faster                                                  |
| mako                     | 9.87 ms                                                | 6.44 ms: 1.53x faster                                                  |
| richards_super           | 57.8 ms                                                | 37.8 ms: 1.53x faster                                                  |
| go                       | 151 ms                                                 | 98.8 ms: 1.53x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.55 us: 1.50x faster                                                  |
| scimark_sor              | 128 ms                                                 | 87.0 ms: 1.47x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 134 us: 1.45x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 45.8 ms: 1.43x faster                                                  |
| richards                 | 48.7 ms                                                | 34.0 ms: 1.43x faster                                                  |
| float                    | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 459 ms: 1.41x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 880 us: 1.41x faster                                                   |
| nbody                    | 93.0 ms                                                | 65.9 ms: 1.41x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.18 us: 1.40x faster                                                  |
| logging_format           | 4.83 us                                                | 3.46 us: 1.40x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.36x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 70.1 ms: 1.35x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.07 ms: 1.35x faster                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.59 ms: 1.34x faster                                                  |
| thrift                   | 572 us                                                 | 426 us: 1.34x faster                                                   |
| xml_etree_process        | 46.5 ms                                                | 34.8 ms: 1.33x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 54.6 ms: 1.32x faster                                                  |
| html5lib                 | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                  |
| pyflate                  | 427 ms                                                 | 332 ms: 1.29x faster                                                   |
| pylint                   | 277 ms                                                 | 215 ms: 1.28x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 1.02 sec: 1.28x faster                                                 |
| generators               | 32.3 ms                                                | 25.3 ms: 1.28x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 502 ms: 1.28x faster                                                   |
| pycparser                | 877 ms                                                 | 689 ms: 1.27x faster                                                   |
| comprehensions           | 16.9 us                                                | 13.3 us: 1.27x faster                                                  |
| regex_compile            | 95.3 ms                                                | 75.3 ms: 1.27x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.6 ms: 1.25x faster                                                  |
| hexiom                   | 6.19 ms                                                | 5.00 ms: 1.24x faster                                                  |
| regex_dna                | 174 ms                                                 | 143 ms: 1.22x faster                                                   |
| dulwich_log              | 35.3 ms                                                | 29.3 ms: 1.21x faster                                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 61.8 ms: 1.19x faster                                                  |
| scimark_fft              | 224 ms                                                 | 190 ms: 1.18x faster                                                   |
| django_template          | 26.4 ms                                                | 22.9 ms: 1.15x faster                                                  |
| fannkuch                 | 303 ms                                                 | 263 ms: 1.15x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 80.2 ms: 1.15x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.13 ms: 1.14x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 474 us: 1.11x faster                                                   |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                 |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.09x faster                                                  |
| sympy_str                | 165 ms                                                 | 152 ms: 1.09x faster                                                   |
| nqueens                  | 63.8 ms                                                | 58.8 ms: 1.08x faster                                                  |
| sympy_expand             | 269 ms                                                 | 249 ms: 1.08x faster                                                   |
| json                     | 3.08 ms                                                | 2.86 ms: 1.08x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 49.6 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.18 ms: 1.08x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.05x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 12.6 ms: 1.04x faster                                                  |
| 2to3                     | 192 ms                                                 | 184 ms: 1.04x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 75.2 ms: 1.03x faster                                                  |
| genshi_text              | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 187 ms: 1.02x faster                                                   |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.48 ms: 1.01x slower                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 37.7 ms: 1.03x slower                                                  |
| coverage                 | 41.5 ms                                                | 43.9 ms: 1.06x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.94 ms: 1.24x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 42.4 ms: 1.25x slower                                                  |
| telco                    | 3.49 ms                                                | 4.45 ms: 1.27x slower                                                  |
| async_generators         | 231 ms                                                 | 295 ms: 1.28x slower                                                   |
| create_gc_cycles         | 860 us                                                 | 1.32 ms: 1.53x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 62.2 ms: 1.66x slower                                                  |
| python_startup           | 10.9 ms                                                | 18.8 ms: 1.73x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 14.4 ms: 1.83x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (2): tornado_http, xml_etree_parse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.227x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.42x