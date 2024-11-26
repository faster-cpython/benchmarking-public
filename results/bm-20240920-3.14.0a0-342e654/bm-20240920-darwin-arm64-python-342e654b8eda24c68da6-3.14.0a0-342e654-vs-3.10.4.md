# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: darwin-arm64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 0.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| docutils       | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                |
| html5lib       | 42.4 ms                                                | 30.0 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 198 ms: 1.96x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 246 ms: 1.92x faster                                                  |
| async_tree_io           | 980 ms                                                 | 579 ms: 1.69x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 459 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.1 ms: 1.55x faster                                                 |
| float          | 69.0 ms                                                | 48.4 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.2 ms: 1.42x faster                                                 |
| regex_dna      | 174 ms                                                 | 146 ms: 1.19x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.53 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 141 us: 1.38x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.31 ms: 1.29x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.5 ms: 1.24x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 52.6 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 73.7 ms: 1.02x slower                                                 |
| json_loads           | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| unpickle             | 8.80 us                                                | 9.12 us: 1.04x slower                                                 |
| pickle               | 6.97 us                                                | 7.39 us: 1.06x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.94 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 13.9 ms: 1.28x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 11.0 ms: 1.39x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.33x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.06 ms: 1.40x faster                                                 |
| django_template | 26.4 ms                                                | 20.1 ms: 1.31x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.0 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.2 us: 3.50x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.29x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.7 us: 2.07x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| async_tree_none          | 388 ms                                                 | 198 ms: 1.96x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.9 ns: 1.93x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 246 ms: 1.92x faster                                                  |
| go                       | 151 ms                                                 | 79.1 ms: 1.91x faster                                                 |
| deepcopy                 | 272 us                                                 | 146 us: 1.86x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.6 ms: 1.85x faster                                                 |
| async_tree_io            | 980 ms                                                 | 579 ms: 1.69x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 737 us: 1.69x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.9 ms: 1.61x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 409 ms: 1.61x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 900 us: 1.60x faster                                                  |
| scimark_lu               | 103 ms                                                 | 64.8 ms: 1.59x faster                                                 |
| generators               | 32.3 ms                                                | 20.7 ms: 1.56x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.56x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.55x faster                                                 |
| nbody                    | 93.0 ms                                                | 60.1 ms: 1.55x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 42.6 ms: 1.54x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.05 ms: 1.53x faster                                                 |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                                  |
| richards                 | 48.7 ms                                                | 32.0 ms: 1.52x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.02 us: 1.47x faster                                                 |
| unpack_sequence          | 39.0 ns                                                | 26.6 ns: 1.47x faster                                                 |
| logging_format           | 4.83 us                                                | 3.32 us: 1.46x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 66.0 ms: 1.44x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.2 ms: 1.43x faster                                                 |
| float                    | 69.0 ms                                                | 48.4 ms: 1.43x faster                                                 |
| regex_compile            | 95.3 ms                                                | 67.2 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 459 ms: 1.42x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.0 ms: 1.41x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 932 ms: 1.40x faster                                                  |
| mako                     | 9.87 ms                                                | 7.06 ms: 1.40x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 458 ms: 1.40x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 141 us: 1.38x faster                                                  |
| scimark_sor              | 128 ms                                                 | 93.1 ms: 1.38x faster                                                 |
| pycparser                | 877 ms                                                 | 639 ms: 1.37x faster                                                  |
| thrift                   | 572 us                                                 | 420 us: 1.36x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 68.8 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 320 ms: 1.33x faster                                                  |
| django_template          | 26.4 ms                                                | 20.1 ms: 1.31x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 27.1 ms: 1.30x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.31 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.28x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.70 ms: 1.27x faster                                                 |
| genshi_text              | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                 |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                                  |
| scimark_fft              | 224 ms                                                 | 179 ms: 1.25x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 37.5 ms: 1.24x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                |
| nqueens                  | 63.8 ms                                                | 53.2 ms: 1.20x faster                                                 |
| regex_dna                | 174 ms                                                 | 146 ms: 1.19x faster                                                  |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                                  |
| 2to3                     | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.0 ms: 1.18x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 452 us: 1.17x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| fannkuch                 | 303 ms                                                 | 262 ms: 1.15x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.0 ms: 1.13x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.6 ms: 1.09x faster                                                 |
| json                     | 3.08 ms                                                | 2.91 ms: 1.06x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 52.6 ms: 1.02x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 73.7 ms: 1.02x slower                                                 |
| json_loads               | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.53 ms: 1.03x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.12 us: 1.04x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 901 us: 1.05x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                 |
| pickle                   | 6.97 us                                                | 7.39 us: 1.06x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.3 ms: 1.07x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.94 us: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 278 ms: 1.20x slower                                                  |
| python_startup           | 10.9 ms                                                | 13.9 ms: 1.28x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 48.1 ms: 1.29x slower                                                 |
| telco                    | 3.49 ms                                                | 4.74 ms: 1.36x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 11.0 ms: 1.39x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (3): tornado_http, xml_etree_parse, pidigits
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-darwin-arm64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.308x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 0.54x