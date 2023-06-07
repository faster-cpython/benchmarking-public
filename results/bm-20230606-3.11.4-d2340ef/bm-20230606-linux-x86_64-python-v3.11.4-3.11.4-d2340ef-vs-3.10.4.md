
# Results vs. 3.10.4

- fork: python
- ref: v3.11.4
- machine: linux-x86_64
- commit hash: d2340ef
- commit date: 2023-06-06
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 258 ms: 1.30x faster                                   |
| chameleon      | 9.06 ms                                                | 6.58 ms: 1.38x faster                                  |
| docutils       | 3.17 sec                                               | 2.57 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 64.2 ms: 1.34x faster                                  |
| tornado_http   | 127 ms                                                 | 96.6 ms: 1.32x faster                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 77.1 ms: 1.43x faster                                  |
| nbody          | 142 ms                                                 | 99.4 ms: 1.43x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.45 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 302 us: 1.51x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 53.9 ms: 1.39x faster                                  |
| tomli_loads          | 2.92 sec                                               | 2.19 sec: 1.33x faster                                 |
| unpickle_pure_python | 300 us                                                 | 229 us: 1.31x faster                                   |
| xml_etree_generate   | 94.2 ms                                                | 76.5 ms: 1.23x faster                                  |
| pickle_list          | 4.56 us                                                | 4.01 us: 1.14x faster                                  |
| json_loads           | 28.8 us                                                | 26.2 us: 1.10x faster                                  |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                  |
| json_dumps           | 13.5 ms                                                | 12.6 ms: 1.07x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| pickle               | 10.3 us                                                | 9.76 us: 1.05x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 160 ms: 1.02x faster                                   |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.53 ms: 1.66x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.01 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.80 ms: 1.51x faster                                  |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                  |
| genshi_text     | 30.3 ms                                                | 22.4 ms: 1.36x faster                                  |
| genshi_xml      | 63.3 ms                                                | 51.8 ms: 1.22x faster                                  |
| Geometric mean  | (ref)                                                  | 1.36x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-linux-x86_64-python-v3.11.4-3.11.4-d2340ef |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue                | 7.42 ms                                                | 3.71 ms: 2.00x faster                                  |
| logging_silent           | 175 ns                                                 | 103 ns: 1.70x faster                                   |
| scimark_sor              | 197 ms                                                 | 118 ms: 1.67x faster                                   |
| python_startup           | 14.2 ms                                                | 8.53 ms: 1.66x faster                                  |
| go                       | 229 ms                                                 | 140 ms: 1.64x faster                                   |
| scimark_monte_carlo      | 108 ms                                                 | 67.7 ms: 1.60x faster                                  |
| pyflate                  | 673 ms                                                 | 421 ms: 1.60x faster                                   |
| crypto_pyaes             | 118 ms                                                 | 74.6 ms: 1.59x faster                                  |
| raytrace                 | 464 ms                                                 | 294 ms: 1.58x faster                                   |
| spectral_norm            | 150 ms                                                 | 97.1 ms: 1.54x faster                                  |
| richards                 | 74.9 ms                                                | 48.5 ms: 1.54x faster                                  |
| chaos                    | 106 ms                                                 | 70.2 ms: 1.51x faster                                  |
| richards_super           | 90.7 ms                                                | 60.0 ms: 1.51x faster                                  |
| pickle_pure_python       | 455 us                                                 | 302 us: 1.51x faster                                   |
| mako                     | 14.8 ms                                                | 9.80 ms: 1.51x faster                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.37 ms: 1.50x faster                                  |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                   |
| unpack_sequence          | 64.7 ns                                                | 43.6 ns: 1.48x faster                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.67 ms: 1.47x faster                                  |
| hexiom                   | 9.53 ms                                                | 6.50 ms: 1.47x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 36.5 us: 1.44x faster                                  |
| float                    | 111 ms                                                 | 77.1 ms: 1.43x faster                                  |
| nbody                    | 142 ms                                                 | 99.4 ms: 1.43x faster                                  |
| django_template          | 45.9 ms                                                | 33.0 ms: 1.39x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 53.9 ms: 1.39x faster                                  |
| chameleon                | 9.06 ms                                                | 6.58 ms: 1.38x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.29 sec: 1.37x faster                                 |
| async_tree_none          | 717 ms                                                 | 523 ms: 1.37x faster                                   |
| pprint_pformat           | 1.99 sec                                               | 1.45 sec: 1.37x faster                                 |
| genshi_text              | 30.3 ms                                                | 22.4 ms: 1.36x faster                                  |
| logging_format           | 8.91 us                                                | 6.58 us: 1.35x faster                                  |
| pprint_safe_repr         | 955 ms                                                 | 707 ms: 1.35x faster                                   |
| thrift                   | 1.03 ms                                                | 771 us: 1.34x faster                                   |
| async_tree_memoization   | 854 ms                                                 | 638 ms: 1.34x faster                                   |
| html5lib                 | 85.9 ms                                                | 64.2 ms: 1.34x faster                                  |
| tomli_loads              | 2.92 sec                                               | 2.19 sec: 1.33x faster                                 |
| logging_simple           | 8.07 us                                                | 6.09 us: 1.33x faster                                  |
| tornado_http             | 127 ms                                                 | 96.6 ms: 1.32x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 229 us: 1.31x faster                                   |
| 2to3                     | 336 ms                                                 | 258 ms: 1.30x faster                                   |
| deepcopy_reduce          | 3.82 us                                                | 2.94 us: 1.30x faster                                  |
| scimark_fft              | 424 ms                                                 | 326 ms: 1.30x faster                                   |
| regex_compile            | 177 ms                                                 | 136 ms: 1.30x faster                                   |
| deepcopy                 | 442 us                                                 | 341 us: 1.29x faster                                   |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 738 ms: 1.29x faster                                   |
| pycparser                | 1.50 sec                                               | 1.18 sec: 1.27x faster                                 |
| aiohttp                  | 1.38 ms                                                | 1.09 ms: 1.26x faster                                  |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                   |
| gunicorn                 | 1.46 ms                                                | 1.17 ms: 1.25x faster                                  |
| docutils                 | 3.17 sec                                               | 2.57 sec: 1.24x faster                                 |
| sqlglot_optimize         | 65.3 ms                                                | 53.0 ms: 1.23x faster                                  |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                   |
| xml_etree_generate       | 94.2 ms                                                | 76.5 ms: 1.23x faster                                  |
| coroutines               | 31.8 ms                                                | 25.9 ms: 1.23x faster                                  |
| genshi_xml               | 63.3 ms                                                | 51.8 ms: 1.22x faster                                  |
| nqueens                  | 100 ms                                                 | 83.1 ms: 1.20x faster                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 139 ms: 1.19x faster                                   |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.58 ms: 1.19x faster                                  |
| comprehensions           | 26.8 us                                                | 22.6 us: 1.19x faster                                  |
| sqlalchemy_imperative    | 21.2 ms                                                | 17.9 ms: 1.19x faster                                  |
| async_generators         | 425 ms                                                 | 361 ms: 1.18x faster                                   |
| dask                     | 423 ms                                                 | 360 ms: 1.17x faster                                   |
| sqlite_synth             | 2.93 us                                                | 2.51 us: 1.17x faster                                  |
| sympy_integrate          | 24.3 ms                                                | 20.9 ms: 1.16x faster                                  |
| bench_thread_pool        | 947 us                                                 | 816 us: 1.16x faster                                   |
| dulwich_log              | 75.9 ms                                                | 65.5 ms: 1.16x faster                                  |
| sympy_expand             | 545 ms                                                 | 470 ms: 1.16x faster                                   |
| flaskblogging            | 8.27 ms                                                | 7.17 ms: 1.15x faster                                  |
| pickle_list              | 4.56 us                                                | 4.01 us: 1.14x faster                                  |
| pylint                   | 525 ms                                                 | 462 ms: 1.14x faster                                   |
| sympy_str                | 328 ms                                                 | 290 ms: 1.13x faster                                   |
| regex_v8                 | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                  |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.0 ms: 1.11x faster                                  |
| sympy_sum                | 185 ms                                                 | 166 ms: 1.11x faster                                   |
| regex_dna                | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| json_loads               | 28.8 us                                                | 26.2 us: 1.10x faster                                  |
| djangocms                | 35.9 us                                                | 33.0 us: 1.09x faster                                  |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                   |
| mdp                      | 2.82 sec                                               | 2.60 sec: 1.08x faster                                 |
| unpickle                 | 14.1 us                                                | 13.1 us: 1.08x faster                                  |
| json_dumps               | 13.5 ms                                                | 12.6 ms: 1.07x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| pickle                   | 10.3 us                                                | 9.76 us: 1.05x faster                                  |
| generators               | 76.8 ms                                                | 73.7 ms: 1.04x faster                                  |
| typing_runtime_protocols | 510 us                                                 | 495 us: 1.03x faster                                   |
| xml_etree_parse          | 163 ms                                                 | 160 ms: 1.02x faster                                   |
| asyncio_tcp              | 925 ms                                                 | 922 ms: 1.00x faster                                   |
| pidigits                 | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| telco                    | 6.54 ms                                                | 6.62 ms: 1.01x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.01 ms: 1.03x slower                                  |
| unpickle_list            | 4.82 us                                                | 5.02 us: 1.04x slower                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 3.15 sec: 1.05x slower                                 |
| gc_traversal             | 3.84 ms                                                | 4.04 ms: 1.05x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.45 ms: 1.07x slower                                  |
| pickle_dict              | 27.3 us                                                | 30.7 us: 1.13x slower                                  |
| mypy2                    | 428 ms                                                 | 534 ms: 1.25x slower                                   |
| Geometric mean           | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: coverage
