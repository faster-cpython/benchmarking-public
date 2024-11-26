# Results vs. 3.10.4

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.106x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 0.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 249 ms: 1.30x slower                                                  |
| docutils       | 1.73 sec                                               | 1.76 sec: 1.02x slower                                                |
| html5lib       | 42.4 ms                                                | 53.2 ms: 1.26x slower                                                 |
| tornado_http   | 86.7 ms                                                | 104 ms: 1.20x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 530 ms: 1.85x faster                                                  |
| async_tree_none         | 388 ms                                                 | 235 ms: 1.65x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 292 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 490 ms: 1.33x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.60x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 69.0 ms                                                | 93.0 ms: 1.35x slower                                                 |
| nbody          | 93.0 ms                                                | 154 ms: 1.66x slower                                                  |
| Geometric mean | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 146 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.51 ms: 1.02x slower                                                 |
| regex_compile  | 95.3 ms                                                | 119 ms: 1.25x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.91 ms: 1.03x faster                                                 |
| pickle               | 6.97 us                                                | 7.03 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 75.9 ms: 1.05x slower                                                 |
| unpickle             | 8.80 us                                                | 9.46 us: 1.08x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.97 us: 1.08x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.5 us: 1.09x slower                                                 |
| json_loads           | 16.4 us                                                | 18.5 us: 1.13x slower                                                 |
| tomli_loads          | 1.71 sec                                               | 1.99 sec: 1.17x slower                                                |
| xml_etree_process    | 46.5 ms                                                | 56.3 ms: 1.21x slower                                                 |
| unpickle_list        | 2.69 us                                                | 3.26 us: 1.21x slower                                                 |
| pickle_pure_python   | 281 us                                                 | 346 us: 1.23x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 67.9 ms: 1.27x slower                                                 |
| unpickle_pure_python | 194 us                                                 | 262 us: 1.35x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.4 ms: 1.60x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.9 ms: 1.76x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.68x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 13.3 ms: 1.35x slower                                                 |
| django_template | 26.4 ms                                                | 36.1 ms: 1.37x slower                                                 |
| genshi_text     | 17.3 ms                                                | 24.7 ms: 1.42x slower                                                 |
| genshi_xml      | 33.8 ms                                                | 49.8 ms: 1.47x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.40x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 142 us: 2.28x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 103 ms: 1.85x faster                                                  |
| async_tree_io            | 980 ms                                                 | 530 ms: 1.85x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 385 ms: 1.71x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 239 ms: 1.71x faster                                                  |
| async_tree_none          | 388 ms                                                 | 235 ms: 1.65x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 292 ms: 1.62x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 490 ms: 1.33x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.23 sec: 1.30x faster                                                |
| pylint                   | 277 ms                                                 | 217 ms: 1.28x faster                                                  |
| create_gc_cycles         | 860 us                                                 | 679 us: 1.27x faster                                                  |
| regex_dna                | 174 ms                                                 | 146 ms: 1.20x faster                                                  |
| gc_traversal             | 2.36 ms                                                | 2.05 ms: 1.15x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 30.6 us: 1.13x faster                                                 |
| deepcopy                 | 272 us                                                 | 243 us: 1.12x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.91 ms: 1.03x faster                                                 |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle                   | 6.97 us                                                | 7.03 us: 1.01x slower                                                 |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| docutils                 | 1.73 sec                                               | 1.76 sec: 1.02x slower                                                |
| regex_effbot             | 2.46 ms                                                | 2.51 ms: 1.02x slower                                                 |
| pathlib                  | 24.5 ms                                                | 25.1 ms: 1.02x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.52 us: 1.04x slower                                                 |
| pycparser                | 877 ms                                                 | 915 ms: 1.04x slower                                                  |
| deepcopy_reduce          | 2.33 us                                                | 2.45 us: 1.05x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 75.9 ms: 1.05x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.46 us: 1.08x slower                                                 |
| json                     | 3.08 ms                                                | 3.33 ms: 1.08x slower                                                 |
| crypto_pyaes             | 71.8 ms                                                | 77.8 ms: 1.08x slower                                                 |
| generators               | 32.3 ms                                                | 35.0 ms: 1.08x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.97 us: 1.08x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.5 us: 1.09x slower                                                 |
| comprehensions           | 16.9 us                                                | 18.7 us: 1.11x slower                                                 |
| richards_super           | 57.8 ms                                                | 64.7 ms: 1.12x slower                                                 |
| json_loads               | 16.4 us                                                | 18.5 us: 1.13x slower                                                 |
| chaos                    | 65.8 ms                                                | 74.7 ms: 1.13x slower                                                 |
| deltablue                | 4.91 ms                                                | 5.61 ms: 1.14x slower                                                 |
| meteor_contest           | 77.7 ms                                                | 88.9 ms: 1.14x slower                                                 |
| richards                 | 48.7 ms                                                | 55.6 ms: 1.14x slower                                                 |
| pyflate                  | 427 ms                                                 | 490 ms: 1.15x slower                                                  |
| mdp                      | 1.63 sec                                               | 1.88 sec: 1.15x slower                                                |
| logging_silent           | 117 ns                                                 | 136 ns: 1.16x slower                                                  |
| dulwich_log              | 35.3 ms                                                | 40.9 ms: 1.16x slower                                                 |
| tomli_loads              | 1.71 sec                                               | 1.99 sec: 1.17x slower                                                |
| thrift                   | 572 us                                                 | 667 us: 1.17x slower                                                  |
| fannkuch                 | 303 ms                                                 | 354 ms: 1.17x slower                                                  |
| scimark_fft              | 224 ms                                                 | 266 ms: 1.19x slower                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 4.07 ms: 1.19x slower                                                 |
| coroutines               | 20.7 ms                                                | 24.7 ms: 1.19x slower                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 78.4 ms: 1.20x slower                                                 |
| nqueens                  | 63.8 ms                                                | 76.4 ms: 1.20x slower                                                 |
| tornado_http             | 86.7 ms                                                | 104 ms: 1.20x slower                                                  |
| go                       | 151 ms                                                 | 182 ms: 1.21x slower                                                  |
| xml_etree_process        | 46.5 ms                                                | 56.3 ms: 1.21x slower                                                 |
| unpickle_list            | 2.69 us                                                | 3.26 us: 1.21x slower                                                 |
| pickle_pure_python       | 281 us                                                 | 346 us: 1.23x slower                                                  |
| raytrace                 | 301 ms                                                 | 373 ms: 1.24x slower                                                  |
| sympy_integrate          | 13.1 ms                                                | 16.3 ms: 1.24x slower                                                 |
| hexiom                   | 6.19 ms                                                | 7.74 ms: 1.25x slower                                                 |
| regex_compile            | 95.3 ms                                                | 119 ms: 1.25x slower                                                  |
| html5lib                 | 42.4 ms                                                | 53.2 ms: 1.26x slower                                                 |
| spectral_norm            | 94.8 ms                                                | 119 ms: 1.26x slower                                                  |
| pprint_safe_repr         | 641 ms                                                 | 810 ms: 1.26x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.65 sec: 1.27x slower                                                |
| xml_etree_generate       | 53.5 ms                                                | 67.9 ms: 1.27x slower                                                 |
| scimark_sor              | 128 ms                                                 | 164 ms: 1.28x slower                                                  |
| 2to3                     | 192 ms                                                 | 249 ms: 1.30x slower                                                  |
| coverage                 | 41.5 ms                                                | 54.4 ms: 1.31x slower                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.90 ms: 1.31x slower                                                 |
| sqlglot_parse            | 1.24 ms                                                | 1.65 ms: 1.33x slower                                                 |
| mako                     | 9.87 ms                                                | 13.3 ms: 1.35x slower                                                 |
| float                    | 69.0 ms                                                | 93.0 ms: 1.35x slower                                                 |
| unpickle_pure_python     | 194 us                                                 | 262 us: 1.35x slower                                                  |
| django_template          | 26.4 ms                                                | 36.1 ms: 1.37x slower                                                 |
| logging_simple           | 4.45 us                                                | 6.10 us: 1.37x slower                                                 |
| logging_format           | 4.83 us                                                | 6.64 us: 1.37x slower                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 51.6 ms: 1.40x slower                                                 |
| scimark_lu               | 103 ms                                                 | 145 ms: 1.41x slower                                                  |
| sympy_str                | 165 ms                                                 | 233 ms: 1.41x slower                                                  |
| genshi_text              | 17.3 ms                                                | 24.7 ms: 1.42x slower                                                 |
| async_generators         | 231 ms                                                 | 332 ms: 1.44x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 49.8 ms: 1.47x slower                                                 |
| bench_thread_pool        | 527 us                                                 | 798 us: 1.51x slower                                                  |
| sympy_sum                | 92.2 ms                                                | 141 ms: 1.53x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 57.2 ms: 1.53x slower                                                 |
| telco                    | 3.49 ms                                                | 5.42 ms: 1.55x slower                                                 |
| sympy_expand             | 269 ms                                                 | 427 ms: 1.59x slower                                                  |
| python_startup           | 10.9 ms                                                | 17.4 ms: 1.60x slower                                                 |
| nbody                    | 93.0 ms                                                | 154 ms: 1.66x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.9 ms: 1.76x slower                                                 |
| unpack_sequence          | 39.0 ns                                                | 96.0 ns: 2.46x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.12x slower                                                          |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.106x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 0.60x