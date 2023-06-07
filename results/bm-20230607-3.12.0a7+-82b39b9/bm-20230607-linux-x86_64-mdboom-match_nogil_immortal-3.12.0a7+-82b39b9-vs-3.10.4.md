
# Results vs. 3.10.4

- fork: mdboom
- ref: match_nogil_immortal
- machine: linux-x86_64
- commit hash: 82b39b9
- commit date: 2023-06-07
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 260 ms: 1.30x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.91 ms: 1.31x faster                                                  |
| docutils       | 3.17 sec                                               | 2.35 sec: 1.35x faster                                                 |
| html5lib       | 85.9 ms                                                | 62.9 ms: 1.37x faster                                                  |
| tornado_http   | 127 ms                                                 | 102 ms: 1.24x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 69.2 ms: 1.60x faster                                                  |
| nbody          | 142 ms                                                 | 91.3 ms: 1.55x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                  |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 314 us: 1.45x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 79.5 ms: 1.40x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.70 ms: 1.39x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.37x faster                                                   |
| tomli_loads          | 2.92 sec                                               | 2.18 sec: 1.34x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 56.6 ms: 1.32x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 124 ms: 1.31x faster                                                   |
| xml_etree_generate   | 94.2 ms                                                | 78.4 ms: 1.20x faster                                                  |
| json_loads           | 28.8 us                                                | 24.9 us: 1.16x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.36 us: 1.04x faster                                                  |
| unpickle             | 14.1 us                                                | 14.5 us: 1.03x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.09 us: 1.06x slower                                                  |
| pickle_dict          | 27.3 us                                                | 29.9 us: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.83 ms: 1.60x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                  |
| genshi_text     | 30.3 ms                                                | 23.0 ms: 1.32x faster                                                  |
| django_template | 45.9 ms                                                | 35.6 ms: 1.29x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 49.2 ms: 1.29x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230607-linux-x86_64-mdboom-match_nogil_immortal-3.12.0a7+-82b39b9 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 523 ms: 3.39x faster                                                   |
| async_tree_none          | 717 ms                                                 | 262 ms: 2.74x faster                                                   |
| async_tree_memoization   | 854 ms                                                 | 318 ms: 2.69x faster                                                   |
| generators               | 76.8 ms                                                | 30.7 ms: 2.50x faster                                                  |
| typing_runtime_protocols | 510 us                                                 | 216 us: 2.36x faster                                                   |
| deltablue                | 7.42 ms                                                | 3.55 ms: 2.09x faster                                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 469 ms: 2.03x faster                                                   |
| asyncio_tcp              | 925 ms                                                 | 512 ms: 1.81x faster                                                   |
| logging_silent           | 175 ns                                                 | 97.5 ns: 1.80x faster                                                  |
| richards                 | 74.9 ms                                                | 44.0 ms: 1.70x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                                 |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                                   |
| richards_super           | 90.7 ms                                                | 55.0 ms: 1.65x faster                                                  |
| python_startup           | 14.2 ms                                                | 8.83 ms: 1.60x faster                                                  |
| float                    | 111 ms                                                 | 69.2 ms: 1.60x faster                                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.29 ms: 1.59x faster                                                  |
| chaos                    | 106 ms                                                 | 68.0 ms: 1.56x faster                                                  |
| scimark_sor              | 197 ms                                                 | 126 ms: 1.55x faster                                                   |
| nbody                    | 142 ms                                                 | 91.3 ms: 1.55x faster                                                  |
| raytrace                 | 464 ms                                                 | 304 ms: 1.52x faster                                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                                  |
| crypto_pyaes             | 118 ms                                                 | 78.0 ms: 1.52x faster                                                  |
| hexiom                   | 9.53 ms                                                | 6.34 ms: 1.50x faster                                                  |
| scimark_monte_carlo      | 108 ms                                                 | 72.5 ms: 1.49x faster                                                  |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.48x faster                                                   |
| pyflate                  | 673 ms                                                 | 459 ms: 1.47x faster                                                   |
| pickle_pure_python       | 455 us                                                 | 314 us: 1.45x faster                                                   |
| pycparser                | 1.50 sec                                               | 1.05 sec: 1.43x faster                                                 |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.41x faster                                                   |
| xml_etree_iterparse      | 111 ms                                                 | 79.5 ms: 1.40x faster                                                  |
| json_dumps               | 13.5 ms                                                | 9.70 ms: 1.39x faster                                                  |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                  |
| unpickle_pure_python     | 300 us                                                 | 218 us: 1.37x faster                                                   |
| html5lib                 | 85.9 ms                                                | 62.9 ms: 1.37x faster                                                  |
| coroutines               | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.35 sec: 1.35x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 38.9 us: 1.35x faster                                                  |
| tomli_loads              | 2.92 sec                                               | 2.18 sec: 1.34x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.33x faster                                                 |
| xml_etree_process        | 74.9 ms                                                | 56.6 ms: 1.32x faster                                                  |
| genshi_text              | 30.3 ms                                                | 23.0 ms: 1.32x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 124 ms: 1.31x faster                                                   |
| chameleon                | 9.06 ms                                                | 6.91 ms: 1.31x faster                                                  |
| pprint_safe_repr         | 955 ms                                                 | 732 ms: 1.30x faster                                                   |
| unpack_sequence          | 64.7 ns                                                | 49.8 ns: 1.30x faster                                                  |
| 2to3                     | 336 ms                                                 | 260 ms: 1.30x faster                                                   |
| django_template          | 45.9 ms                                                | 35.6 ms: 1.29x faster                                                  |
| genshi_xml               | 63.3 ms                                                | 49.2 ms: 1.29x faster                                                  |
| logging_simple           | 8.07 us                                                | 6.31 us: 1.28x faster                                                  |
| thrift                   | 1.03 ms                                                | 812 us: 1.27x faster                                                   |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                                   |
| logging_format           | 8.91 us                                                | 7.00 us: 1.27x faster                                                  |
| fannkuch                 | 486 ms                                                 | 390 ms: 1.25x faster                                                   |
| tornado_http             | 127 ms                                                 | 102 ms: 1.24x faster                                                   |
| nqueens                  | 100 ms                                                 | 80.5 ms: 1.24x faster                                                  |
| deepcopy                 | 442 us                                                 | 361 us: 1.22x faster                                                   |
| sqlglot_normalize        | 135 ms                                                 | 112 ms: 1.21x faster                                                   |
| regex_compile            | 177 ms                                                 | 146 ms: 1.21x faster                                                   |
| xml_etree_generate       | 94.2 ms                                                | 78.4 ms: 1.20x faster                                                  |
| scimark_fft              | 424 ms                                                 | 353 ms: 1.20x faster                                                   |
| deepcopy_reduce          | 3.82 us                                                | 3.20 us: 1.20x faster                                                  |
| aiohttp                  | 1.38 ms                                                | 1.16 ms: 1.19x faster                                                  |
| pylint                   | 525 ms                                                 | 441 ms: 1.19x faster                                                   |
| sqlglot_optimize         | 65.3 ms                                                | 55.1 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.62 ms: 1.18x faster                                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 140 ms: 1.18x faster                                                   |
| gunicorn                 | 1.46 ms                                                | 1.25 ms: 1.17x faster                                                  |
| json_loads               | 28.8 us                                                | 24.9 us: 1.16x faster                                                  |
| comprehensions           | 26.8 us                                                | 23.4 us: 1.15x faster                                                  |
| regex_v8                 | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                  |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                                  |
| pathlib                  | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 67.5 ms: 1.12x faster                                                  |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.8 ms: 1.12x faster                                                  |
| bench_thread_pool        | 947 us                                                 | 846 us: 1.12x faster                                                   |
| sympy_integrate          | 24.3 ms                                                | 21.9 ms: 1.11x faster                                                  |
| mdp                      | 2.82 sec                                               | 2.56 sec: 1.10x faster                                                 |
| sympy_expand             | 545 ms                                                 | 495 ms: 1.10x faster                                                   |
| sqlite_synth             | 2.93 us                                                | 2.68 us: 1.10x faster                                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.53 ms: 1.09x faster                                                  |
| djangocms                | 35.9 us                                                | 33.5 us: 1.07x faster                                                  |
| regex_dna                | 222 ms                                                 | 209 ms: 1.06x faster                                                   |
| sympy_str                | 328 ms                                                 | 310 ms: 1.06x faster                                                   |
| pickle_list              | 4.56 us                                                | 4.36 us: 1.04x faster                                                  |
| async_generators         | 425 ms                                                 | 411 ms: 1.03x faster                                                   |
| gc_traversal             | 3.84 ms                                                | 3.72 ms: 1.03x faster                                                  |
| sympy_sum                | 185 ms                                                 | 180 ms: 1.03x faster                                                   |
| unpickle                 | 14.1 us                                                | 14.5 us: 1.03x slower                                                  |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| regex_effbot             | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                  |
| unpickle_list            | 4.82 us                                                | 5.09 us: 1.06x slower                                                  |
| telco                    | 6.54 ms                                                | 6.92 ms: 1.06x slower                                                  |
| pickle_dict              | 27.3 us                                                | 29.9 us: 1.10x slower                                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                  |
| dask                     | 423 ms                                                 | 500 ms: 1.18x slower                                                   |
| coverage                 | 72.8 ms                                                | 104 ms: 1.43x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (3): meteor_contest, pickle, bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging
