
# Results vs. 3.10.4

- fork: brandtbucher
- ref: eval_frame
- machine: linux-x86_64
- commit hash: 26d9521
- commit date: 2023-05-11
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                               |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.17x faster                                             |
| tornado_http   | 127 ms                                                 | 99.3 ms: 1.28x faster                                              |
| Geometric mean | (ref)                                                  | 1.23x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.5 ms: 1.56x faster                                              |
| float          | 111 ms                                                 | 81.8 ms: 1.35x faster                                              |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.29x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                               |
| regex_v8       | 25.0 ms                                                | 20.9 ms: 1.20x faster                                              |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                               |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 314 us: 1.45x faster                                               |
| unpickle_pure_python | 300 us                                                 | 220 us: 1.36x faster                                               |
| json_dumps           | 13.5 ms                                                | 10.0 ms: 1.35x faster                                              |
| tomli_loads          | 2.92 sec                                               | 2.22 sec: 1.32x faster                                             |
| xml_etree_process    | 74.9 ms                                                | 59.2 ms: 1.27x faster                                              |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 85.6 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.05x faster                                               |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                              |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                              |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                              |
| pickle_list          | 4.56 us                                                | 4.80 us: 1.05x slower                                              |
| pickle_dict          | 27.3 us                                                | 32.2 us: 1.18x slower                                              |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.18 ms: 1.54x faster                                              |
| python_startup_no_site | 5.82 ms                                                | 6.71 ms: 1.15x slower                                              |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.36x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.50x faster                                               |
| generators               | 76.8 ms                                                | 32.2 ms: 2.38x faster                                              |
| deltablue                | 7.42 ms                                                | 3.52 ms: 2.11x faster                                              |
| asyncio_tcp              | 925 ms                                                 | 516 ms: 1.79x faster                                               |
| richards_super           | 90.7 ms                                                | 51.0 ms: 1.78x faster                                              |
| logging_silent           | 175 ns                                                 | 102 ns: 1.72x faster                                               |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                               |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                             |
| richards                 | 74.9 ms                                                | 45.1 ms: 1.66x faster                                              |
| chaos                    | 106 ms                                                 | 65.4 ms: 1.63x faster                                              |
| scimark_sor              | 197 ms                                                 | 123 ms: 1.60x faster                                               |
| nbody                    | 142 ms                                                 | 90.5 ms: 1.56x faster                                              |
| raytrace                 | 464 ms                                                 | 300 ms: 1.55x faster                                               |
| python_startup           | 14.2 ms                                                | 9.18 ms: 1.54x faster                                              |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.54x faster                                              |
| hexiom                   | 9.53 ms                                                | 6.22 ms: 1.53x faster                                              |
| crypto_pyaes             | 118 ms                                                 | 77.5 ms: 1.53x faster                                              |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                             |
| async_tree_none          | 717 ms                                                 | 471 ms: 1.52x faster                                               |
| pyflate                  | 673 ms                                                 | 448 ms: 1.50x faster                                               |
| async_tree_memoization   | 854 ms                                                 | 575 ms: 1.49x faster                                               |
| scimark_monte_carlo      | 108 ms                                                 | 73.0 ms: 1.48x faster                                              |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.47x faster                                              |
| pickle_pure_python       | 455 us                                                 | 314 us: 1.45x faster                                               |
| scimark_lu               | 163 ms                                                 | 114 ms: 1.43x faster                                               |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.42x faster                                               |
| coroutines               | 31.8 ms                                                | 22.7 ms: 1.40x faster                                              |
| unpack_sequence          | 64.7 ns                                                | 46.7 ns: 1.39x faster                                              |
| deepcopy_memo            | 52.3 us                                                | 37.9 us: 1.38x faster                                              |
| unpickle_pure_python     | 300 us                                                 | 220 us: 1.36x faster                                               |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.36x faster                                              |
| float                    | 111 ms                                                 | 81.8 ms: 1.35x faster                                              |
| json_dumps               | 13.5 ms                                                | 10.0 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 710 ms: 1.34x faster                                               |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.32x faster                                             |
| tomli_loads              | 2.92 sec                                               | 2.22 sec: 1.32x faster                                             |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                             |
| pprint_safe_repr         | 955 ms                                                 | 733 ms: 1.30x faster                                               |
| logging_simple           | 8.07 us                                                | 6.23 us: 1.30x faster                                              |
| tornado_http             | 127 ms                                                 | 99.3 ms: 1.28x faster                                              |
| logging_format           | 8.91 us                                                | 6.94 us: 1.28x faster                                              |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.28x faster                                              |
| xml_etree_process        | 74.9 ms                                                | 59.2 ms: 1.27x faster                                              |
| fannkuch                 | 486 ms                                                 | 386 ms: 1.26x faster                                               |
| 2to3                     | 336 ms                                                 | 269 ms: 1.25x faster                                               |
| deepcopy                 | 442 us                                                 | 354 us: 1.25x faster                                               |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.24x faster                                               |
| mypy2                    | 428 ms                                                 | 346 ms: 1.24x faster                                               |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                               |
| sqlglot_optimize         | 65.3 ms                                                | 53.9 ms: 1.21x faster                                              |
| nqueens                  | 100 ms                                                 | 82.6 ms: 1.21x faster                                              |
| deepcopy_reduce          | 3.82 us                                                | 3.16 us: 1.21x faster                                              |
| regex_v8                 | 25.0 ms                                                | 20.9 ms: 1.20x faster                                              |
| scimark_fft              | 424 ms                                                 | 361 ms: 1.17x faster                                               |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.17x faster                                             |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                              |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.5 ms: 1.14x faster                                              |
| bench_thread_pool        | 947 us                                                 | 829 us: 1.14x faster                                               |
| sqlalchemy_declarative   | 165 ms                                                 | 145 ms: 1.14x faster                                               |
| json                     | 5.42 ms                                                | 4.76 ms: 1.14x faster                                              |
| dulwich_log              | 75.9 ms                                                | 67.8 ms: 1.12x faster                                              |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.12x faster                                              |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                             |
| xml_etree_generate       | 94.2 ms                                                | 85.6 ms: 1.10x faster                                              |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.98 ms: 1.10x faster                                              |
| regex_dna                | 222 ms                                                 | 203 ms: 1.09x faster                                               |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                               |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                              |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.07x faster                                              |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                               |
| xml_etree_parse          | 163 ms                                                 | 155 ms: 1.05x faster                                               |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                               |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                              |
| unpickle_list            | 4.82 us                                                | 4.91 us: 1.02x slower                                              |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                              |
| gc_traversal             | 3.84 ms                                                | 3.93 ms: 1.02x slower                                              |
| telco                    | 6.54 ms                                                | 6.84 ms: 1.05x slower                                              |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.05x slower                                              |
| pickle_list              | 4.56 us                                                | 4.80 us: 1.05x slower                                              |
| async_generators         | 425 ms                                                 | 456 ms: 1.07x slower                                               |
| regex_effbot             | 3.23 ms                                                | 3.53 ms: 1.09x slower                                              |
| python_startup_no_site   | 5.82 ms                                                | 6.71 ms: 1.15x slower                                              |
| pickle_dict              | 27.3 us                                                | 32.2 us: 1.18x slower                                              |
| dask                     | 423 ms                                                 | 539 ms: 1.27x slower                                               |
| coverage                 | 72.8 ms                                                | 96.0 ms: 1.32x slower                                              |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                       |
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
