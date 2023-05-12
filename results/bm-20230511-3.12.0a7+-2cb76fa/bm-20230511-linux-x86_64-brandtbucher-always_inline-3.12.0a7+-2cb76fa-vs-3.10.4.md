
# Results vs. 3.10.4

- fork: brandtbucher
- ref: always_inline
- machine: linux-x86_64
- commit hash: 2cb76fa
- commit date: 2023-05-11
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                                  |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.17x faster                                                |
| tornado_http   | 127 ms                                                 | 99.6 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.8 ms: 1.60x faster                                                 |
| float          | 111 ms                                                 | 82.0 ms: 1.35x faster                                                 |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                  |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                 |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                  |
| regex_effbot   | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 314 us: 1.45x faster                                                  |
| json_dumps           | 13.5 ms                                                | 9.79 ms: 1.38x faster                                                 |
| unpickle_pure_python | 300 us                                                 | 219 us: 1.37x faster                                                  |
| tomli_loads          | 2.92 sec                                               | 2.19 sec: 1.33x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.26x faster                                                 |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                                 |
| xml_etree_generate   | 94.2 ms                                                | 85.7 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                  |
| unpickle_list        | 4.82 us                                                | 4.86 us: 1.01x slower                                                 |
| pickle_list          | 4.56 us                                                | 4.64 us: 1.02x slower                                                 |
| unpickle             | 14.1 us                                                | 14.6 us: 1.03x slower                                                 |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                 |
| pickle_dict          | 27.3 us                                                | 32.8 us: 1.20x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.20 ms: 1.54x faster                                                 |
| python_startup_no_site | 5.82 ms                                                | 6.71 ms: 1.15x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-always_inline-3.12.0a7+-2cb76fa |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.44x faster                                                  |
| generators               | 76.8 ms                                                | 31.2 ms: 2.46x faster                                                 |
| deltablue                | 7.42 ms                                                | 3.58 ms: 2.07x faster                                                 |
| asyncio_tcp              | 925 ms                                                 | 516 ms: 1.79x faster                                                  |
| richards_super           | 90.7 ms                                                | 51.1 ms: 1.77x faster                                                 |
| logging_silent           | 175 ns                                                 | 103 ns: 1.70x faster                                                  |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                                  |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                                |
| richards                 | 74.9 ms                                                | 44.9 ms: 1.67x faster                                                 |
| chaos                    | 106 ms                                                 | 65.6 ms: 1.62x faster                                                 |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.60x faster                                                  |
| nbody                    | 142 ms                                                 | 88.8 ms: 1.60x faster                                                 |
| python_startup           | 14.2 ms                                                | 9.20 ms: 1.54x faster                                                 |
| hexiom                   | 9.53 ms                                                | 6.21 ms: 1.53x faster                                                 |
| raytrace                 | 464 ms                                                 | 302 ms: 1.53x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                                |
| sqlglot_parse            | 2.06 ms                                                | 1.35 ms: 1.53x faster                                                 |
| async_tree_none          | 717 ms                                                 | 471 ms: 1.52x faster                                                  |
| pyflate                  | 673 ms                                                 | 444 ms: 1.52x faster                                                  |
| crypto_pyaes             | 118 ms                                                 | 78.1 ms: 1.52x faster                                                 |
| async_tree_memoization   | 854 ms                                                 | 573 ms: 1.49x faster                                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.67 ms: 1.47x faster                                                 |
| scimark_monte_carlo      | 108 ms                                                 | 74.0 ms: 1.46x faster                                                 |
| pickle_pure_python       | 455 us                                                 | 314 us: 1.45x faster                                                  |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                                  |
| scimark_lu               | 163 ms                                                 | 118 ms: 1.39x faster                                                  |
| coroutines               | 31.8 ms                                                | 23.0 ms: 1.39x faster                                                 |
| json_dumps               | 13.5 ms                                                | 9.79 ms: 1.38x faster                                                 |
| unpack_sequence          | 64.7 ns                                                | 47.1 ns: 1.37x faster                                                 |
| unpickle_pure_python     | 300 us                                                 | 219 us: 1.37x faster                                                  |
| mako                     | 14.8 ms                                                | 10.8 ms: 1.37x faster                                                 |
| deepcopy_memo            | 52.3 us                                                | 38.8 us: 1.35x faster                                                 |
| float                    | 111 ms                                                 | 82.0 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 711 ms: 1.34x faster                                                  |
| tomli_loads              | 2.92 sec                                               | 2.19 sec: 1.33x faster                                                |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.32x faster                                                |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                |
| pprint_safe_repr         | 955 ms                                                 | 736 ms: 1.30x faster                                                  |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.29x faster                                                 |
| tornado_http             | 127 ms                                                 | 99.6 ms: 1.28x faster                                                 |
| logging_simple           | 8.07 us                                                | 6.34 us: 1.27x faster                                                 |
| logging_format           | 8.91 us                                                | 7.04 us: 1.27x faster                                                 |
| xml_etree_process        | 74.9 ms                                                | 59.2 ms: 1.26x faster                                                 |
| fannkuch                 | 486 ms                                                 | 385 ms: 1.26x faster                                                  |
| 2to3                     | 336 ms                                                 | 269 ms: 1.25x faster                                                  |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                                  |
| mypy2                    | 428 ms                                                 | 347 ms: 1.24x faster                                                  |
| deepcopy                 | 442 us                                                 | 358 us: 1.23x faster                                                  |
| nqueens                  | 100 ms                                                 | 82.0 ms: 1.22x faster                                                 |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 53.9 ms: 1.21x faster                                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                                 |
| regex_v8                 | 25.0 ms                                                | 21.0 ms: 1.19x faster                                                 |
| scimark_fft              | 424 ms                                                 | 359 ms: 1.18x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.17x faster                                                |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                                 |
| bench_thread_pool        | 947 us                                                 | 827 us: 1.15x faster                                                  |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.5 ms: 1.14x faster                                                 |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.82 ms: 1.13x faster                                                 |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                                 |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                 |
| dulwich_log              | 75.9 ms                                                | 68.0 ms: 1.12x faster                                                 |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                |
| xml_etree_generate       | 94.2 ms                                                | 85.7 ms: 1.10x faster                                                 |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| regex_dna                | 222 ms                                                 | 203 ms: 1.09x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                 |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.08x faster                                                  |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                 |
| xml_etree_parse          | 163 ms                                                 | 154 ms: 1.06x faster                                                  |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                  |
| gc_traversal             | 3.84 ms                                                | 3.83 ms: 1.00x faster                                                 |
| unpickle_list            | 4.82 us                                                | 4.86 us: 1.01x slower                                                 |
| pickle_list              | 4.56 us                                                | 4.64 us: 1.02x slower                                                 |
| unpickle                 | 14.1 us                                                | 14.6 us: 1.03x slower                                                 |
| telco                    | 6.54 ms                                                | 6.78 ms: 1.04x slower                                                 |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                                 |
| async_generators         | 425 ms                                                 | 459 ms: 1.08x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 3.52 ms: 1.09x slower                                                 |
| python_startup_no_site   | 5.82 ms                                                | 6.71 ms: 1.15x slower                                                 |
| pickle_dict              | 27.3 us                                                | 32.8 us: 1.20x slower                                                 |
| dask                     | 423 ms                                                 | 538 ms: 1.27x slower                                                  |
| coverage                 | 72.8 ms                                                | 96.5 ms: 1.33x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
