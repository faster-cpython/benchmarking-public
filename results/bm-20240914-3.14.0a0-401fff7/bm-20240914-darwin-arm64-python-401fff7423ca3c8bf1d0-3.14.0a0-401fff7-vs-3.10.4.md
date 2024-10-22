# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 0.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 159 ms: 1.20x faster                                                  |
| docutils       | 1.73 sec                                               | 1.40 sec: 1.24x faster                                                |
| html5lib       | 42.4 ms                                                | 30.1 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 199 ms: 1.95x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 247 ms: 1.92x faster                                                  |
| async_tree_io           | 980 ms                                                 | 580 ms: 1.69x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 460 ms: 1.41x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.0 ms: 1.55x faster                                                 |
| float          | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.2 ms: 1.42x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.4 ms: 1.04x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.44 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 181 us: 1.55x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 140 us: 1.39x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.43 ms: 1.26x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.6 ms: 1.24x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.16x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 52.7 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 73.7 ms: 1.02x slower                                                 |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| unpickle             | 8.80 us                                                | 9.24 us: 1.05x slower                                                 |
| pickle               | 6.97 us                                                | 7.42 us: 1.06x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.94 us: 1.07x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.92 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.0 ms: 1.56x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.8 ms: 1.75x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.65x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.93 ms: 1.42x faster                                                 |
| django_template | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.4 us: 3.42x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.12 ms: 2.32x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.5 us: 2.10x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| async_tree_none          | 388 ms                                                 | 199 ms: 1.95x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.7 ns: 1.93x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 247 ms: 1.92x faster                                                  |
| go                       | 151 ms                                                 | 79.2 ms: 1.90x faster                                                 |
| deepcopy                 | 272 us                                                 | 145 us: 1.88x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.8 ms: 1.84x faster                                                 |
| richards_super           | 57.8 ms                                                | 34.2 ms: 1.69x faster                                                 |
| async_tree_io            | 980 ms                                                 | 580 ms: 1.69x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 743 us: 1.67x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 905 us: 1.59x faster                                                  |
| generators               | 32.3 ms                                                | 20.5 ms: 1.57x faster                                                 |
| richards                 | 48.7 ms                                                | 31.1 ms: 1.57x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.56x faster                                                 |
| nbody                    | 93.0 ms                                                | 60.0 ms: 1.55x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 181 us: 1.55x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                 |
| pylint                   | 277 ms                                                 | 180 ms: 1.53x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.05 ms: 1.53x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.1 ms: 1.52x faster                                                 |
| scimark_lu               | 103 ms                                                 | 67.8 ms: 1.52x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 440 ms: 1.50x faster                                                  |
| unpack_sequence          | 39.0 ns                                                | 26.4 ns: 1.48x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.02 us: 1.47x faster                                                 |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.1 ms: 1.43x faster                                                 |
| mako                     | 9.87 ms                                                | 6.93 ms: 1.42x faster                                                 |
| float                    | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| regex_compile            | 95.3 ms                                                | 67.2 ms: 1.42x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.0 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 460 ms: 1.41x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.1 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 460 ms: 1.39x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 938 ms: 1.39x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 140 us: 1.39x faster                                                  |
| pycparser                | 877 ms                                                 | 637 ms: 1.38x faster                                                  |
| scimark_sor              | 128 ms                                                 | 93.1 ms: 1.38x faster                                                 |
| thrift                   | 572 us                                                 | 420 us: 1.36x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 68.4 ms: 1.35x faster                                                 |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                  |
| django_template          | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 27.2 ms: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.2 ms: 1.28x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.43 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                                  |
| genshi_text              | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 37.6 ms: 1.24x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.40 sec: 1.24x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.77 ms: 1.24x faster                                                 |
| scimark_fft              | 224 ms                                                 | 183 ms: 1.22x faster                                                  |
| regex_dna                | 174 ms                                                 | 145 ms: 1.21x faster                                                  |
| 2to3                     | 192 ms                                                 | 159 ms: 1.20x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.3 ms: 1.20x faster                                                 |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 448 us: 1.18x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.4 ms: 1.17x faster                                                 |
| fannkuch                 | 303 ms                                                 | 260 ms: 1.16x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.16x faster                                                |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 169 ms: 1.12x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.8 ms: 1.08x faster                                                 |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.4 ms: 1.04x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 52.7 ms: 1.01x faster                                                 |
| regex_effbot             | 2.46 ms                                                | 2.44 ms: 1.01x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 73.7 ms: 1.02x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 895 us: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.24 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.0 ms: 1.06x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                                 |
| pickle                   | 6.97 us                                                | 7.42 us: 1.06x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.94 us: 1.07x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.92 us: 1.08x slower                                                 |
| async_generators         | 231 ms                                                 | 278 ms: 1.20x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 49.7 ms: 1.33x slower                                                 |
| telco                    | 3.49 ms                                                | 4.71 ms: 1.35x slower                                                 |
| python_startup           | 10.9 ms                                                | 17.0 ms: 1.56x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.8 ms: 1.75x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 0.52x