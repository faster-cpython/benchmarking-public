# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: darwin-arm64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.230x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 183 ms: 1.05x faster                                       |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.10x faster                                     |
| html5lib       | 42.4 ms                                                | 34.2 ms: 1.24x faster                                      |
| tornado_http   | 86.7 ms                                                | 75.3 ms: 1.15x faster                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 199 ms: 1.95x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 246 ms: 1.93x faster                                       |
| async_tree_io           | 980 ms                                                 | 584 ms: 1.68x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 459 ms: 1.42x faster                                       |
| Geometric mean          | (ref)                                                  | 1.73x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 69.0 ms                                                | 48.2 ms: 1.43x faster                                      |
| nbody          | 93.0 ms                                                | 65.3 ms: 1.43x faster                                      |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.8 ms: 1.27x faster                                      |
| regex_dna      | 174 ms                                                 | 148 ms: 1.18x faster                                       |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                      |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 178 us: 1.57x faster                                       |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.48x faster                                       |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.37x faster                                     |
| xml_etree_process    | 46.5 ms                                                | 34.8 ms: 1.34x faster                                      |
| json_dumps           | 8.11 ms                                                | 7.13 ms: 1.14x faster                                      |
| xml_etree_generate   | 53.5 ms                                                | 50.4 ms: 1.06x faster                                      |
| json_loads           | 16.4 us                                                | 16.5 us: 1.01x slower                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 73.1 ms: 1.01x slower                                      |
| unpickle             | 8.80 us                                                | 9.02 us: 1.03x slower                                      |
| pickle               | 6.97 us                                                | 7.33 us: 1.05x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| pickle_list          | 2.74 us                                                | 2.95 us: 1.08x slower                                      |
| unpickle_list        | 2.69 us                                                | 2.97 us: 1.10x slower                                      |
| Geometric mean       | (ref)                                                  | 1.10x faster                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.0 ms: 1.75x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 14.6 ms: 1.85x slower                                      |
| Geometric mean         | (ref)                                                  | 1.80x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.46 ms: 1.53x faster                                      |
| django_template | 26.4 ms                                                | 23.0 ms: 1.15x faster                                      |
| genshi_text     | 17.3 ms                                                | 16.6 ms: 1.04x faster                                      |
| genshi_xml      | 33.8 ms                                                | 42.3 ms: 1.25x slower                                      |
| Geometric mean  | (ref)                                                  | 1.10x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.8 us: 3.30x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.07x faster                                      |
| deltablue                | 4.91 ms                                                | 2.38 ms: 2.06x faster                                      |
| async_tree_none          | 388 ms                                                 | 199 ms: 1.95x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 246 ms: 1.93x faster                                       |
| raytrace                 | 301 ms                                                 | 171 ms: 1.76x faster                                       |
| deepcopy                 | 272 us                                                 | 154 us: 1.76x faster                                       |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                       |
| logging_silent           | 117 ns                                                 | 69.8 ns: 1.68x faster                                      |
| async_tree_io            | 980 ms                                                 | 584 ms: 1.68x faster                                       |
| scimark_lu               | 103 ms                                                 | 64.6 ms: 1.59x faster                                      |
| chaos                    | 65.8 ms                                                | 41.5 ms: 1.58x faster                                      |
| pickle_pure_python       | 281 us                                                 | 178 us: 1.57x faster                                       |
| go                       | 151 ms                                                 | 97.6 ms: 1.54x faster                                      |
| mako                     | 9.87 ms                                                | 6.46 ms: 1.53x faster                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.53 us: 1.52x faster                                      |
| richards_super           | 57.8 ms                                                | 38.7 ms: 1.50x faster                                      |
| scimark_sor              | 128 ms                                                 | 86.0 ms: 1.49x faster                                      |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.48x faster                                       |
| asyncio_tcp              | 659 ms                                                 | 456 ms: 1.45x faster                                       |
| scimark_monte_carlo      | 65.6 ms                                                | 45.5 ms: 1.44x faster                                      |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.43x faster                                      |
| float                    | 69.0 ms                                                | 48.2 ms: 1.43x faster                                      |
| nbody                    | 93.0 ms                                                | 65.3 ms: 1.43x faster                                      |
| sqlglot_parse            | 1.24 ms                                                | 875 us: 1.42x faster                                       |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 459 ms: 1.42x faster                                       |
| logging_format           | 4.83 us                                                | 3.42 us: 1.41x faster                                      |
| richards                 | 48.7 ms                                                | 35.0 ms: 1.39x faster                                      |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.37x faster                                     |
| spectral_norm            | 94.8 ms                                                | 69.3 ms: 1.37x faster                                      |
| sqlglot_transpile        | 1.44 ms                                                | 1.06 ms: 1.36x faster                                      |
| thrift                   | 572 us                                                 | 426 us: 1.34x faster                                       |
| xml_etree_process        | 46.5 ms                                                | 34.8 ms: 1.34x faster                                      |
| crypto_pyaes             | 71.8 ms                                                | 54.0 ms: 1.33x faster                                      |
| pprint_safe_repr         | 641 ms                                                 | 483 ms: 1.33x faster                                       |
| pprint_pformat           | 1.30 sec                                               | 990 ms: 1.32x faster                                       |
| pyflate                  | 427 ms                                                 | 325 ms: 1.32x faster                                       |
| pylint                   | 277 ms                                                 | 212 ms: 1.31x faster                                       |
| pycparser                | 877 ms                                                 | 678 ms: 1.29x faster                                       |
| comprehensions           | 16.9 us                                                | 13.1 us: 1.29x faster                                      |
| generators               | 32.3 ms                                                | 25.4 ms: 1.28x faster                                      |
| regex_compile            | 95.3 ms                                                | 74.8 ms: 1.27x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.96 ms: 1.25x faster                                      |
| coroutines               | 20.7 ms                                                | 16.7 ms: 1.24x faster                                      |
| html5lib                 | 42.4 ms                                                | 34.2 ms: 1.24x faster                                      |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.24x faster                                     |
| dulwich_log              | 35.3 ms                                                | 28.9 ms: 1.22x faster                                      |
| regex_dna                | 174 ms                                                 | 148 ms: 1.18x faster                                       |
| scimark_fft              | 224 ms                                                 | 190 ms: 1.18x faster                                       |
| sympy_sum                | 92.2 ms                                                | 79.4 ms: 1.16x faster                                      |
| tornado_http             | 86.7 ms                                                | 75.3 ms: 1.15x faster                                      |
| django_template          | 26.4 ms                                                | 23.0 ms: 1.15x faster                                      |
| json_dumps               | 8.11 ms                                                | 7.13 ms: 1.14x faster                                      |
| fannkuch                 | 303 ms                                                 | 269 ms: 1.13x faster                                       |
| bench_thread_pool        | 527 us                                                 | 474 us: 1.11x faster                                       |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.10x faster                                     |
| sympy_str                | 165 ms                                                 | 151 ms: 1.10x faster                                       |
| sympy_expand             | 269 ms                                                 | 246 ms: 1.09x faster                                       |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.09x faster                                      |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.14 ms: 1.09x faster                                      |
| nqueens                  | 63.8 ms                                                | 58.8 ms: 1.08x faster                                      |
| xml_etree_generate       | 53.5 ms                                                | 50.4 ms: 1.06x faster                                      |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                      |
| sympy_integrate          | 13.1 ms                                                | 12.5 ms: 1.05x faster                                      |
| 2to3                     | 192 ms                                                 | 183 ms: 1.05x faster                                       |
| meteor_contest           | 77.7 ms                                                | 74.4 ms: 1.05x faster                                      |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.04x faster                                     |
| genshi_text              | 17.3 ms                                                | 16.6 ms: 1.04x faster                                      |
| sqlglot_normalize        | 190 ms                                                 | 186 ms: 1.02x faster                                       |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                      |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| json_loads               | 16.4 us                                                | 16.5 us: 1.01x slower                                      |
| sqlglot_optimize         | 36.8 ms                                                | 37.1 ms: 1.01x slower                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 73.1 ms: 1.01x slower                                      |
| unpickle                 | 8.80 us                                                | 9.02 us: 1.03x slower                                      |
| pickle                   | 6.97 us                                                | 7.33 us: 1.05x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                      |
| coverage                 | 41.5 ms                                                | 43.8 ms: 1.06x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.61 ms: 1.06x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| pickle_list              | 2.74 us                                                | 2.95 us: 1.08x slower                                      |
| unpickle_list            | 2.69 us                                                | 2.97 us: 1.10x slower                                      |
| gc_traversal             | 2.36 ms                                                | 2.94 ms: 1.24x slower                                      |
| genshi_xml               | 33.8 ms                                                | 42.3 ms: 1.25x slower                                      |
| async_generators         | 231 ms                                                 | 292 ms: 1.26x slower                                       |
| telco                    | 3.49 ms                                                | 4.57 ms: 1.31x slower                                      |
| create_gc_cycles         | 860 us                                                 | 1.30 ms: 1.52x slower                                      |
| bench_mp_pool            | 37.4 ms                                                | 61.8 ms: 1.65x slower                                      |
| python_startup           | 10.9 ms                                                | 19.0 ms: 1.75x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 14.6 ms: 1.85x slower                                      |
| unpack_sequence          | 39.0 ns                                                | 76.0 ns: 1.95x slower                                      |
| Geometric mean           | (ref)                                                  | 1.20x faster                                               |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-darwin-arm64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.230x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.43x