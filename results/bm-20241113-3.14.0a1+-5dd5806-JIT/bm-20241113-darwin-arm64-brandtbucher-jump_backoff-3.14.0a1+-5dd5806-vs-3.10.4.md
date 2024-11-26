# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backoff
- machine: darwin-arm64
- commit hash: 5dd5806
- commit date: 2024-11-13
- overall geometric mean: 1.230x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 177 ms: 1.08x faster                                                 |
| docutils       | 1.73 sec                                               | 1.55 sec: 1.12x faster                                               |
| html5lib       | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                |
| Geometric mean | (ref)                                                  | 1.16x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 206 ms: 1.88x faster                                                 |
| async_tree_memoization  | 474 ms                                                 | 254 ms: 1.86x faster                                                 |
| async_tree_io           | 980 ms                                                 | 591 ms: 1.66x faster                                                 |
| async_tree_cpu_io_mixed | 649 ms                                                 | 468 ms: 1.39x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.69x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.0 ms: 1.48x faster                                                |
| float          | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.4 ms: 1.30x faster                                                |
| regex_dna      | 174 ms                                                 | 136 ms: 1.28x faster                                                 |
| regex_v8       | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                |
| regex_effbot   | 2.46 ms                                                | 2.33 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.18x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                 | 122 us: 1.59x faster                                                 |
| pickle_pure_python   | 281 us                                                 | 194 us: 1.45x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.36x faster                                               |
| xml_etree_process    | 46.5 ms                                                | 35.3 ms: 1.32x faster                                                |
| json_dumps           | 8.11 ms                                                | 7.11 ms: 1.14x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 49.8 ms: 1.07x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                 |
| json_loads           | 16.4 us                                                | 16.5 us: 1.01x slower                                                |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.7 ms: 1.81x slower                                                |
| python_startup_no_site | 7.91 ms                                                | 15.0 ms: 1.89x slower                                                |
| Geometric mean         | (ref)                                                  | 1.85x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.23 ms: 1.58x faster                                                |
| django_template | 26.4 ms                                                | 22.3 ms: 1.18x faster                                                |
| genshi_text     | 17.3 ms                                                | 15.7 ms: 1.10x faster                                                |
| genshi_xml      | 33.8 ms                                                | 38.6 ms: 1.14x slower                                                |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 99.2 us: 3.26x faster                                                |
| deepcopy_memo            | 34.7 us                                                | 17.6 us: 1.97x faster                                                |
| deltablue                | 4.91 ms                                                | 2.59 ms: 1.89x faster                                                |
| async_tree_none          | 388 ms                                                 | 206 ms: 1.88x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 254 ms: 1.86x faster                                                 |
| deepcopy                 | 272 us                                                 | 158 us: 1.72x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.69x faster                                                 |
| async_tree_io            | 980 ms                                                 | 591 ms: 1.66x faster                                                 |
| raytrace                 | 301 ms                                                 | 186 ms: 1.62x faster                                                 |
| logging_silent           | 117 ns                                                 | 73.8 ns: 1.59x faster                                                |
| unpickle_pure_python     | 194 us                                                 | 122 us: 1.59x faster                                                 |
| mako                     | 9.87 ms                                                | 6.23 ms: 1.58x faster                                                |
| richards_super           | 57.8 ms                                                | 37.3 ms: 1.55x faster                                                |
| chaos                    | 65.8 ms                                                | 43.4 ms: 1.52x faster                                                |
| go                       | 151 ms                                                 | 99.9 ms: 1.51x faster                                                |
| deepcopy_reduce          | 2.33 us                                                | 1.54 us: 1.51x faster                                                |
| scimark_lu               | 103 ms                                                 | 68.9 ms: 1.49x faster                                                |
| nbody                    | 93.0 ms                                                | 63.0 ms: 1.48x faster                                                |
| scimark_sor              | 128 ms                                                 | 87.2 ms: 1.47x faster                                                |
| richards                 | 48.7 ms                                                | 33.4 ms: 1.46x faster                                                |
| scimark_monte_carlo      | 65.6 ms                                                | 45.2 ms: 1.45x faster                                                |
| pickle_pure_python       | 281 us                                                 | 194 us: 1.45x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 873 us: 1.42x faster                                                 |
| pylint                   | 277 ms                                                 | 195 ms: 1.42x faster                                                 |
| float                    | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 468 ms: 1.39x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.06 ms: 1.37x faster                                                |
| spectral_norm            | 94.8 ms                                                | 69.8 ms: 1.36x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.36x faster                                               |
| logging_simple           | 4.45 us                                                | 3.33 us: 1.34x faster                                                |
| pprint_safe_repr         | 641 ms                                                 | 480 ms: 1.34x faster                                                 |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.64 ms: 1.33x faster                                                |
| pprint_pformat           | 1.30 sec                                               | 982 ms: 1.33x faster                                                 |
| logging_format           | 4.83 us                                                | 3.66 us: 1.32x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 35.3 ms: 1.32x faster                                                |
| crypto_pyaes             | 71.8 ms                                                | 54.8 ms: 1.31x faster                                                |
| pycparser                | 877 ms                                                 | 672 ms: 1.30x faster                                                 |
| pyflate                  | 427 ms                                                 | 328 ms: 1.30x faster                                                 |
| html5lib                 | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                |
| regex_compile            | 95.3 ms                                                | 73.4 ms: 1.30x faster                                                |
| thrift                   | 572 us                                                 | 441 us: 1.30x faster                                                 |
| regex_dna                | 174 ms                                                 | 136 ms: 1.28x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.93 ms: 1.26x faster                                                |
| comprehensions           | 16.9 us                                                | 13.7 us: 1.24x faster                                                |
| sqlalchemy_declarative   | 73.3 ms                                                | 59.4 ms: 1.23x faster                                                |
| sympy_sum                | 92.2 ms                                                | 75.8 ms: 1.22x faster                                                |
| dulwich_log              | 35.3 ms                                                | 29.1 ms: 1.21x faster                                                |
| generators               | 32.3 ms                                                | 26.7 ms: 1.21x faster                                                |
| scimark_fft              | 224 ms                                                 | 186 ms: 1.21x faster                                                 |
| coroutines               | 20.7 ms                                                | 17.4 ms: 1.19x faster                                                |
| django_template          | 26.4 ms                                                | 22.3 ms: 1.18x faster                                                |
| json_dumps               | 8.11 ms                                                | 7.11 ms: 1.14x faster                                                |
| sympy_str                | 165 ms                                                 | 147 ms: 1.12x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.55 sec: 1.12x faster                                               |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.08 ms: 1.11x faster                                                |
| genshi_text              | 17.3 ms                                                | 15.7 ms: 1.10x faster                                                |
| sympy_integrate          | 13.1 ms                                                | 12.0 ms: 1.10x faster                                                |
| bench_thread_pool        | 527 us                                                 | 482 us: 1.09x faster                                                 |
| fannkuch                 | 303 ms                                                 | 278 ms: 1.09x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                |
| 2to3                     | 192 ms                                                 | 177 ms: 1.08x faster                                                 |
| json                     | 3.08 ms                                                | 2.86 ms: 1.08x faster                                                |
| xml_etree_generate       | 53.5 ms                                                | 49.8 ms: 1.07x faster                                                |
| meteor_contest           | 77.7 ms                                                | 72.6 ms: 1.07x faster                                                |
| pathlib                  | 24.5 ms                                                | 22.9 ms: 1.07x faster                                                |
| regex_effbot             | 2.46 ms                                                | 2.33 ms: 1.06x faster                                                |
| sqlglot_optimize         | 36.8 ms                                                | 34.9 ms: 1.05x faster                                                |
| sympy_expand             | 269 ms                                                 | 255 ms: 1.05x faster                                                 |
| nqueens                  | 63.8 ms                                                | 61.3 ms: 1.04x faster                                                |
| mdp                      | 1.63 sec                                               | 1.59 sec: 1.03x faster                                               |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.03x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 187 ms: 1.02x faster                                                 |
| json_loads               | 16.4 us                                                | 16.5 us: 1.01x slower                                                |
| pidigits                 | 282 ms                                                 | 284 ms: 1.01x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                |
| coverage                 | 41.5 ms                                                | 44.3 ms: 1.07x slower                                                |
| genshi_xml               | 33.8 ms                                                | 38.6 ms: 1.14x slower                                                |
| gc_traversal             | 2.36 ms                                                | 2.93 ms: 1.24x slower                                                |
| telco                    | 3.49 ms                                                | 4.48 ms: 1.28x slower                                                |
| async_generators         | 231 ms                                                 | 306 ms: 1.32x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 1.33 ms: 1.55x slower                                                |
| bench_mp_pool            | 37.4 ms                                                | 62.2 ms: 1.66x slower                                                |
| python_startup           | 10.9 ms                                                | 19.7 ms: 1.81x slower                                                |
| python_startup_no_site   | 7.91 ms                                                | 15.0 ms: 1.89x slower                                                |
| Geometric mean           | (ref)                                                  | 1.22x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20241113-3.14.0a1+-5dd5806-JIT/bm-20241113-darwin-arm64-brandtbucher-jump_backoff-3.14.0a1+-5dd5806.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.230x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.37x