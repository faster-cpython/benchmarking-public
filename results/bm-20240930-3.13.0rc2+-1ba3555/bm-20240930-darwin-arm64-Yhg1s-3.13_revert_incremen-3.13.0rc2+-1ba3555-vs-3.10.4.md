# Results vs. 3.10.4

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: darwin-arm64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 0.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 174 ms: 1.10x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.75 ms: 1.32x faster                                                  |
| docutils       | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                 |
| html5lib       | 42.4 ms                                                | 34.7 ms: 1.22x faster                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 501 ms: 1.96x faster                                                   |
| async_tree_none         | 388 ms                                                 | 210 ms: 1.85x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 264 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 454 ms: 1.43x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.75x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 54.6 ms: 1.26x faster                                                  |
| nbody          | 93.0 ms                                                | 75.1 ms: 1.24x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 76.1 ms: 1.25x faster                                                  |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                  |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 203 us: 1.38x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 156 us: 1.25x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.56 ms: 1.24x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 40.8 ms: 1.14x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.52 sec: 1.12x faster                                                 |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.0 ms: 1.03x slower                                                  |
| unpickle             | 8.80 us                                                | 9.21 us: 1.05x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 56.3 ms: 1.05x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.86 us: 1.06x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| pickle               | 6.97 us                                                | 7.60 us: 1.09x slower                                                  |
| pickle_list          | 2.74 us                                                | 3.03 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.7 ms: 1.54x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 13.2 ms: 1.67x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.60x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.54 ms: 1.31x faster                                                  |
| django_template | 26.4 ms                                                | 22.1 ms: 1.20x faster                                                  |
| genshi_text     | 17.3 ms                                                | 15.7 ms: 1.11x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 32.7 ms: 1.03x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 99.2 us: 3.26x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.46 ms: 2.00x faster                                                  |
| async_tree_io            | 980 ms                                                 | 501 ms: 1.96x faster                                                   |
| async_tree_none          | 388 ms                                                 | 210 ms: 1.85x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 264 ms: 1.80x faster                                                   |
| raytrace                 | 301 ms                                                 | 173 ms: 1.74x faster                                                   |
| logging_silent           | 117 ns                                                 | 69.5 ns: 1.69x faster                                                  |
| chaos                    | 65.8 ms                                                | 39.6 ms: 1.66x faster                                                  |
| pylint                   | 277 ms                                                 | 179 ms: 1.55x faster                                                   |
| richards_super           | 57.8 ms                                                | 38.4 ms: 1.51x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 838 us: 1.48x faster                                                   |
| asyncio_tcp              | 659 ms                                                 | 456 ms: 1.44x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 454 ms: 1.43x faster                                                   |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.42x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.0 us: 1.41x faster                                                  |
| richards                 | 48.7 ms                                                | 34.6 ms: 1.41x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 203 us: 1.38x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 47.7 ms: 1.37x faster                                                  |
| go                       | 151 ms                                                 | 110 ms: 1.36x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 53.6 ms: 1.34x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 25.9 us: 1.34x faster                                                  |
| scimark_lu               | 103 ms                                                 | 76.9 ms: 1.34x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.70 ms: 1.32x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.75 ms: 1.32x faster                                                  |
| mako                     | 9.87 ms                                                | 7.54 ms: 1.31x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 72.5 ms: 1.31x faster                                                  |
| logging_format           | 4.83 us                                                | 3.75 us: 1.29x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.47 us: 1.28x faster                                                  |
| generators               | 32.3 ms                                                | 25.4 ms: 1.27x faster                                                  |
| float                    | 69.0 ms                                                | 54.6 ms: 1.26x faster                                                  |
| pycparser                | 877 ms                                                 | 698 ms: 1.26x faster                                                   |
| mypy2                    | 607 ms                                                 | 484 ms: 1.25x faster                                                   |
| regex_compile            | 95.3 ms                                                | 76.1 ms: 1.25x faster                                                  |
| thrift                   | 572 us                                                 | 457 us: 1.25x faster                                                   |
| unpickle_pure_python     | 194 us                                                 | 156 us: 1.25x faster                                                   |
| pyflate                  | 427 ms                                                 | 341 ms: 1.25x faster                                                   |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.25x faster                                                 |
| scimark_sor              | 128 ms                                                 | 103 ms: 1.24x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 516 ms: 1.24x faster                                                   |
| nbody                    | 93.0 ms                                                | 75.1 ms: 1.24x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.05 sec: 1.24x faster                                                 |
| unpack_sequence          | 39.0 ns                                                | 31.5 ns: 1.24x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 28.6 ms: 1.24x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.56 ms: 1.24x faster                                                  |
| html5lib                 | 42.4 ms                                                | 34.7 ms: 1.22x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 75.4 ms: 1.22x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                 |
| django_template          | 26.4 ms                                                | 22.1 ms: 1.20x faster                                                  |
| deepcopy                 | 272 us                                                 | 228 us: 1.19x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.92 ms: 1.17x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 11.2 ms: 1.17x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 2.02 us: 1.15x faster                                                  |
| sympy_str                | 165 ms                                                 | 144 ms: 1.15x faster                                                   |
| xml_etree_process        | 46.5 ms                                                | 40.8 ms: 1.14x faster                                                  |
| scimark_fft              | 224 ms                                                 | 197 ms: 1.14x faster                                                   |
| fannkuch                 | 303 ms                                                 | 267 ms: 1.13x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.52 sec: 1.12x faster                                                 |
| coroutines               | 20.7 ms                                                | 18.5 ms: 1.12x faster                                                  |
| genshi_text              | 17.3 ms                                                | 15.7 ms: 1.11x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.47 sec: 1.11x faster                                                 |
| 2to3                     | 192 ms                                                 | 174 ms: 1.10x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 479 us: 1.10x faster                                                   |
| dask                     | 253 ms                                                 | 230 ms: 1.10x faster                                                   |
| sympy_expand             | 269 ms                                                 | 247 ms: 1.09x faster                                                   |
| nqueens                  | 63.8 ms                                                | 59.6 ms: 1.07x faster                                                  |
| gunicorn                 | 1.30 ms                                                | 1.22 ms: 1.07x faster                                                  |
| create_gc_cycles         | 860 us                                                 | 808 us: 1.06x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 73.3 ms: 1.06x faster                                                  |
| aiohttp                  | 1.22 ms                                                | 1.16 ms: 1.06x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 34.8 ms: 1.06x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 32.7 ms: 1.03x faster                                                  |
| json                     | 3.08 ms                                                | 3.01 ms: 1.03x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                  |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.0 ms: 1.03x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.21 us: 1.05x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 56.3 ms: 1.05x slower                                                  |
| unpickle_list            | 2.69 us                                                | 2.86 us: 1.06x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.08x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| pickle                   | 6.97 us                                                | 7.60 us: 1.09x slower                                                  |
| pickle_list              | 2.74 us                                                | 3.03 us: 1.11x slower                                                  |
| coverage                 | 41.5 ms                                                | 46.1 ms: 1.11x slower                                                  |
| async_generators         | 231 ms                                                 | 296 ms: 1.28x slower                                                   |
| bench_mp_pool            | 37.4 ms                                                | 50.7 ms: 1.36x slower                                                  |
| telco                    | 3.49 ms                                                | 4.77 ms: 1.37x slower                                                  |
| flaskblogging            | 2.65 ms                                                | 3.97 ms: 1.50x slower                                                  |
| python_startup           | 10.9 ms                                                | 16.7 ms: 1.54x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.2 ms: 1.67x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.17x faster                                                           |

Benchmark hidden because not significant (5): tornado_http, xml_etree_parse, asyncio_websockets, pidigits, pathlib
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 0.58x