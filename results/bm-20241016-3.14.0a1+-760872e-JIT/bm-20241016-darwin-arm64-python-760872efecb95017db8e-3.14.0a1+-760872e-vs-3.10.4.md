# Results vs. 3.10.4

- fork: python
- ref: 760872efecb95017db8e
- machine: darwin-arm64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 183 ms: 1.05x faster                                                   |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                 |
| html5lib       | 42.4 ms                                                | 33.9 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 197 ms: 1.97x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 243 ms: 1.95x faster                                                   |
| async_tree_io           | 980 ms                                                 | 579 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 455 ms: 1.43x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.74x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 48.3 ms: 1.43x faster                                                  |
| nbody          | 93.0 ms                                                | 65.3 ms: 1.42x faster                                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 75.0 ms: 1.27x faster                                                  |
| regex_dna      | 174 ms                                                 | 148 ms: 1.18x faster                                                   |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 178 us: 1.57x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.47x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 34.5 ms: 1.35x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.12 ms: 1.14x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 50.3 ms: 1.06x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.01x faster                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 72.5 ms: 1.00x slower                                                  |
| unpickle             | 8.80 us                                                | 9.08 us: 1.03x slower                                                  |
| pickle               | 6.97 us                                                | 7.30 us: 1.05x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.94 us: 1.07x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.97 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.9 ms: 1.73x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 14.6 ms: 1.84x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.79x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.47 ms: 1.52x faster                                                  |
| django_template | 26.4 ms                                                | 22.6 ms: 1.17x faster                                                  |
| genshi_text     | 17.3 ms                                                | 16.6 ms: 1.04x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 42.7 ms: 1.26x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.8 us: 3.41x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.07x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.43 ms: 2.02x faster                                                  |
| async_tree_none          | 388 ms                                                 | 197 ms: 1.97x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 243 ms: 1.95x faster                                                   |
| raytrace                 | 301 ms                                                 | 167 ms: 1.80x faster                                                   |
| deepcopy                 | 272 us                                                 | 152 us: 1.78x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.69x faster                                                   |
| async_tree_io            | 980 ms                                                 | 579 ms: 1.69x faster                                                   |
| logging_silent           | 117 ns                                                 | 69.9 ns: 1.68x faster                                                  |
| scimark_lu               | 103 ms                                                 | 64.4 ms: 1.60x faster                                                  |
| chaos                    | 65.8 ms                                                | 41.4 ms: 1.59x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 178 us: 1.57x faster                                                   |
| richards_super           | 57.8 ms                                                | 37.1 ms: 1.56x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.55x faster                                                  |
| go                       | 151 ms                                                 | 98.0 ms: 1.54x faster                                                  |
| mako                     | 9.87 ms                                                | 6.47 ms: 1.52x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 442 ms: 1.49x faster                                                   |
| scimark_sor              | 128 ms                                                 | 86.2 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.47x faster                                                   |
| richards                 | 48.7 ms                                                | 33.4 ms: 1.46x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 45.6 ms: 1.44x faster                                                  |
| float                    | 69.0 ms                                                | 48.3 ms: 1.43x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 455 ms: 1.43x faster                                                   |
| nbody                    | 93.0 ms                                                | 65.3 ms: 1.42x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 875 us: 1.42x faster                                                   |
| logging_format           | 4.83 us                                                | 3.40 us: 1.42x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.13 us: 1.42x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                 |
| thrift                   | 572 us                                                 | 418 us: 1.37x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 69.3 ms: 1.37x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.06 ms: 1.36x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 34.5 ms: 1.35x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 53.9 ms: 1.33x faster                                                  |
| pyflate                  | 427 ms                                                 | 326 ms: 1.31x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 998 ms: 1.31x faster                                                   |
| pylint                   | 277 ms                                                 | 212 ms: 1.30x faster                                                   |
| comprehensions           | 16.9 us                                                | 13.0 us: 1.30x faster                                                  |
| pycparser                | 877 ms                                                 | 678 ms: 1.29x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 497 ms: 1.29x faster                                                   |
| generators               | 32.3 ms                                                | 25.2 ms: 1.28x faster                                                  |
| regex_compile            | 95.3 ms                                                | 75.0 ms: 1.27x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.92 ms: 1.26x faster                                                  |
| html5lib                 | 42.4 ms                                                | 33.9 ms: 1.25x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.6 ms: 1.25x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 28.7 ms: 1.23x faster                                                  |
| regex_dna                | 174 ms                                                 | 148 ms: 1.18x faster                                                   |
| scimark_fft              | 224 ms                                                 | 190 ms: 1.18x faster                                                   |
| django_template          | 26.4 ms                                                | 22.6 ms: 1.17x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 79.7 ms: 1.16x faster                                                  |
| fannkuch                 | 303 ms                                                 | 264 ms: 1.15x faster                                                   |
| json_dumps               | 8.11 ms                                                | 7.12 ms: 1.14x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 472 us: 1.12x faster                                                   |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                 |
| sympy_expand             | 269 ms                                                 | 245 ms: 1.10x faster                                                   |
| pathlib                  | 24.5 ms                                                | 22.3 ms: 1.10x faster                                                  |
| sympy_str                | 165 ms                                                 | 151 ms: 1.10x faster                                                   |
| nqueens                  | 63.8 ms                                                | 58.4 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.14 ms: 1.09x faster                                                  |
| json                     | 3.08 ms                                                | 2.87 ms: 1.07x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 50.3 ms: 1.06x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.54 sec: 1.06x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 12.5 ms: 1.05x faster                                                  |
| 2to3                     | 192 ms                                                 | 183 ms: 1.05x faster                                                   |
| genshi_text              | 17.3 ms                                                | 16.6 ms: 1.04x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 182 ms: 1.04x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 75.2 ms: 1.03x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.01x faster                                                   |
| pidigits                 | 282 ms                                                 | 284 ms: 1.00x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 72.5 ms: 1.00x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.08 us: 1.03x slower                                                  |
| pickle                   | 6.97 us                                                | 7.30 us: 1.05x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 43.9 ms: 1.06x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.94 us: 1.07x slower                                                  |
| unpickle_list            | 2.69 us                                                | 2.97 us: 1.10x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.96 ms: 1.25x slower                                                  |
| async_generators         | 231 ms                                                 | 291 ms: 1.26x slower                                                   |
| genshi_xml               | 33.8 ms                                                | 42.7 ms: 1.26x slower                                                  |
| telco                    | 3.49 ms                                                | 4.54 ms: 1.30x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 1.31 ms: 1.53x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 61.8 ms: 1.65x slower                                                  |
| python_startup           | 10.9 ms                                                | 18.9 ms: 1.73x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 14.6 ms: 1.84x slower                                                  |
| unpack_sequence          | 39.0 ns                                                | 76.0 ns: 1.95x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (3): tornado_http, sqlglot_optimize, json_loads
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.43x