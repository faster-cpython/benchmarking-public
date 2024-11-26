# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.243x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 0.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 176 ms: 1.09x faster                                                  |
| docutils       | 1.73 sec                                               | 1.56 sec: 1.11x faster                                                |
| html5lib       | 42.4 ms                                                | 33.8 ms: 1.25x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 201 ms: 1.93x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 247 ms: 1.92x faster                                                  |
| async_tree_io           | 980 ms                                                 | 589 ms: 1.66x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 459 ms: 1.41x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.72x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.1 ms: 1.50x faster                                                 |
| nbody          | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.3 ms: 1.28x faster                                                 |
| regex_dna      | 174 ms                                                 | 148 ms: 1.18x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.04x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.49 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 178 us: 1.58x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.49x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 34.1 ms: 1.36x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.19 ms: 1.31x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 50.1 ms: 1.07x faster                                                 |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                 |
| unpickle             | 8.80 us                                                | 9.23 us: 1.05x slower                                                 |
| pickle               | 6.97 us                                                | 7.42 us: 1.06x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.92 us: 1.06x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.88 us: 1.07x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.4 ms: 1.33x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 11.5 ms: 1.46x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.45 ms: 1.53x faster                                                 |
| django_template | 26.4 ms                                                | 22.6 ms: 1.17x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.6 ms: 1.04x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 41.1 ms: 1.22x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.3 us: 3.42x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.1 us: 2.16x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.35 ms: 2.09x faster                                                 |
| async_tree_none          | 388 ms                                                 | 201 ms: 1.93x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 247 ms: 1.92x faster                                                  |
| logging_silent           | 117 ns                                                 | 62.8 ns: 1.87x faster                                                 |
| deepcopy                 | 272 us                                                 | 153 us: 1.77x faster                                                  |
| raytrace                 | 301 ms                                                 | 173 ms: 1.75x faster                                                  |
| async_tree_io            | 980 ms                                                 | 589 ms: 1.66x faster                                                  |
| chaos                    | 65.8 ms                                                | 40.1 ms: 1.64x faster                                                 |
| scimark_lu               | 103 ms                                                 | 63.4 ms: 1.62x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 412 ms: 1.60x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 178 us: 1.58x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.55x faster                                                 |
| mako                     | 9.87 ms                                                | 6.45 ms: 1.53x faster                                                 |
| float                    | 69.0 ms                                                | 46.1 ms: 1.50x faster                                                 |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.49x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.02 us: 1.47x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 850 us: 1.46x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                 |
| scimark_sor              | 128 ms                                                 | 87.7 ms: 1.46x faster                                                 |
| logging_format           | 4.83 us                                                | 3.31 us: 1.46x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.0 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 459 ms: 1.41x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.04 ms: 1.39x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 51.7 ms: 1.39x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 47.4 ms: 1.38x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 34.1 ms: 1.36x faster                                                 |
| pylint                   | 277 ms                                                 | 205 ms: 1.35x faster                                                  |
| thrift                   | 572 us                                                 | 425 us: 1.35x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.8 us: 1.32x faster                                                 |
| generators               | 32.3 ms                                                | 24.6 ms: 1.31x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.19 ms: 1.31x faster                                                 |
| pyflate                  | 427 ms                                                 | 326 ms: 1.31x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.74 ms: 1.31x faster                                                 |
| pycparser                | 877 ms                                                 | 678 ms: 1.29x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                                 |
| regex_compile            | 95.3 ms                                                | 74.3 ms: 1.28x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 509 ms: 1.26x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.04 sec: 1.25x faster                                                |
| html5lib                 | 42.4 ms                                                | 33.8 ms: 1.25x faster                                                 |
| richards_super           | 57.8 ms                                                | 46.4 ms: 1.25x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.25x faster                                                |
| sympy_sum                | 92.2 ms                                                | 75.2 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                                 |
| regex_dna                | 174 ms                                                 | 148 ms: 1.18x faster                                                  |
| django_template          | 26.4 ms                                                | 22.6 ms: 1.17x faster                                                 |
| sympy_str                | 165 ms                                                 | 143 ms: 1.15x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.98 ms: 1.15x faster                                                 |
| fannkuch                 | 303 ms                                                 | 263 ms: 1.15x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.5 ms: 1.14x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 469 us: 1.12x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.46 sec: 1.12x faster                                                |
| docutils                 | 1.73 sec                                               | 1.56 sec: 1.11x faster                                                |
| richards                 | 48.7 ms                                                | 44.4 ms: 1.10x faster                                                 |
| nqueens                  | 63.8 ms                                                | 58.2 ms: 1.10x faster                                                 |
| sympy_expand             | 269 ms                                                 | 247 ms: 1.09x faster                                                  |
| 2to3                     | 192 ms                                                 | 176 ms: 1.09x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.9 ms: 1.07x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 50.1 ms: 1.07x faster                                                 |
| json                     | 3.08 ms                                                | 2.91 ms: 1.06x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.6 ms: 1.04x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 183 ms: 1.04x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 35.5 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.04x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 75.2 ms: 1.03x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.49 ms: 1.01x slower                                                 |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.23 us: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 904 us: 1.05x slower                                                  |
| pickle                   | 6.97 us                                                | 7.42 us: 1.06x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.92 us: 1.06x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.88 us: 1.07x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.8 ms: 1.08x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.58 us: 1.09x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 41.1 ms: 1.22x slower                                                 |
| async_generators         | 231 ms                                                 | 290 ms: 1.25x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 49.4 ms: 1.32x slower                                                 |
| python_startup           | 10.9 ms                                                | 14.4 ms: 1.33x slower                                                 |
| telco                    | 3.49 ms                                                | 4.80 ms: 1.38x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 11.5 ms: 1.46x slower                                                 |
| unpack_sequence          | 39.0 ns                                                | 75.9 ns: 1.94x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (3): tornado_http, xml_etree_parse, xml_etree_iterparse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.243x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 0.56x