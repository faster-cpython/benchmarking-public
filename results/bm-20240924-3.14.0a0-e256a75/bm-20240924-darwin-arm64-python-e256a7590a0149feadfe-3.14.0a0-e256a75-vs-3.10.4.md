# Results vs. 3.10.4

- fork: python
- ref: e256a7590a0149feadfe
- machine: darwin-arm64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 0.75x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.20x faster                                                  |
| docutils       | 1.73 sec                                               | 1.42 sec: 1.22x faster                                                |
| html5lib       | 42.4 ms                                                | 30.0 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 198 ms: 1.96x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 247 ms: 1.92x faster                                                  |
| async_tree_io           | 980 ms                                                 | 579 ms: 1.69x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 459 ms: 1.41x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.2 ms: 1.55x faster                                                 |
| float          | 69.0 ms                                                | 48.4 ms: 1.42x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 66.8 ms: 1.43x faster                                                 |
| regex_dna      | 174 ms                                                 | 144 ms: 1.21x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.4 ms: 1.05x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 183 us: 1.54x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 141 us: 1.38x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.26 ms: 1.30x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 73.5 ms: 1.02x slower                                                 |
| json_loads           | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| unpickle             | 8.80 us                                                | 9.05 us: 1.03x slower                                                 |
| pickle               | 6.97 us                                                | 7.39 us: 1.06x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.98 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.7 ms: 1.44x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.53x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.21 ms: 1.37x faster                                                 |
| django_template | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.6 us: 3.49x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.12 ms: 2.32x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.5 us: 2.10x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.01x faster                                                  |
| async_tree_none          | 388 ms                                                 | 198 ms: 1.96x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.3 ns: 1.94x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 247 ms: 1.92x faster                                                  |
| go                       | 151 ms                                                 | 79.2 ms: 1.90x faster                                                 |
| deepcopy                 | 272 us                                                 | 143 us: 1.90x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.6 ms: 1.85x faster                                                 |
| async_tree_io            | 980 ms                                                 | 579 ms: 1.69x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 740 us: 1.68x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 900 us: 1.60x faster                                                  |
| richards_super           | 57.8 ms                                                | 36.2 ms: 1.60x faster                                                 |
| scimark_lu               | 103 ms                                                 | 64.8 ms: 1.59x faster                                                 |
| generators               | 32.3 ms                                                | 20.7 ms: 1.56x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.56x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.56x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 424 ms: 1.55x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 42.4 ms: 1.55x faster                                                 |
| nbody                    | 93.0 ms                                                | 60.2 ms: 1.55x faster                                                 |
| pylint                   | 277 ms                                                 | 180 ms: 1.54x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 183 us: 1.54x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.06 ms: 1.53x faster                                                 |
| richards                 | 48.7 ms                                                | 32.4 ms: 1.50x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.01 us: 1.48x faster                                                 |
| unpack_sequence          | 39.0 ns                                                | 26.6 ns: 1.47x faster                                                 |
| logging_format           | 4.83 us                                                | 3.30 us: 1.46x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.0 ms: 1.44x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 66.2 ms: 1.43x faster                                                 |
| regex_compile            | 95.3 ms                                                | 66.8 ms: 1.43x faster                                                 |
| float                    | 69.0 ms                                                | 48.4 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 459 ms: 1.41x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.0 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 455 ms: 1.41x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 929 ms: 1.40x faster                                                  |
| scimark_sor              | 128 ms                                                 | 92.6 ms: 1.38x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 141 us: 1.38x faster                                                  |
| pycparser                | 877 ms                                                 | 636 ms: 1.38x faster                                                  |
| mako                     | 9.87 ms                                                | 7.21 ms: 1.37x faster                                                 |
| thrift                   | 572 us                                                 | 424 us: 1.35x faster                                                  |
| pyflate                  | 427 ms                                                 | 319 ms: 1.34x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 69.2 ms: 1.33x faster                                                 |
| django_template          | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.26 ms: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 27.4 ms: 1.29x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.28x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.70 ms: 1.27x faster                                                 |
| genshi_text              | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                 |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                                  |
| scimark_fft              | 224 ms                                                 | 179 ms: 1.26x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.42 sec: 1.22x faster                                                |
| regex_dna                | 174 ms                                                 | 144 ms: 1.21x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.0 ms: 1.20x faster                                                 |
| 2to3                     | 192 ms                                                 | 160 ms: 1.20x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 30.9 ms: 1.19x faster                                                 |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.19x faster                                                  |
| fannkuch                 | 303 ms                                                 | 259 ms: 1.17x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 454 us: 1.16x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.15x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.14x faster                                                |
| genshi_xml               | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.6 ms: 1.09x faster                                                 |
| json                     | 3.08 ms                                                | 2.92 ms: 1.05x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.3 ms: 1.05x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.4 ms: 1.05x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                 |
| regex_effbot             | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 73.5 ms: 1.02x slower                                                 |
| json_loads               | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.05 us: 1.03x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 889 us: 1.03x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.06x slower                                                 |
| pickle                   | 6.97 us                                                | 7.39 us: 1.06x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.1 ms: 1.06x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.98 us: 1.11x slower                                                 |
| async_generators         | 231 ms                                                 | 278 ms: 1.20x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.1 ms: 1.29x slower                                                 |
| telco                    | 3.49 ms                                                | 4.63 ms: 1.33x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.7 ms: 1.44x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (3): tornado_http, asyncio_websockets, xml_etree_parse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 0.75x