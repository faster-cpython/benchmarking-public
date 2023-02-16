
# Results vs. 3.10.4

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: ba16621
- commit date: 2022-12-17
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                     |
| chameleon      | 9.17 ms                                                | 6.26 ms: 1.47x faster                                                    |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                   |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                  | 1.37x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.1 ms: 1.53x faster                                                    |
| float          | 109 ms                                                 | 72.0 ms: 1.51x faster                                                    |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                    |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                     |
| regex_effbot   | 3.19 ms                                                | 3.50 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 281 us: 1.61x faster                                                     |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                     |
| json_dumps           | 13.4 ms                                                | 9.39 ms: 1.43x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                    |
| xml_etree_generate   | 93.8 ms                                                | 76.2 ms: 1.23x faster                                                    |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                    |
| pickle_list          | 4.72 us                                                | 4.10 us: 1.15x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                                     |
| unpickle             | 14.2 us                                                | 13.0 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                                     |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                                    |
| unpickle_list        | 4.92 us                                                | 5.09 us: 1.04x slower                                                    |
| pickle_dict          | 27.6 us                                                | 30.9 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.51 ms: 1.66x faster                                                    |
| python_startup_no_site | 5.78 ms                                                | 6.09 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.42 ms: 1.55x faster                                                    |
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.50x faster                                                    |
| django_template | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                    |
| genshi_xml      | 63.7 ms                                                | 46.9 ms: 1.36x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                                    |
| logging_silent          | 176 ns                                                 | 91.9 ns: 1.92x faster                                                    |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                                     |
| richards                | 75.2 ms                                                | 42.0 ms: 1.79x faster                                                    |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                     |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                     |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                                     |
| python_startup          | 14.1 ms                                                | 8.51 ms: 1.66x faster                                                    |
| scimark_monte_carlo     | 109 ms                                                 | 66.0 ms: 1.64x faster                                                    |
| pickle_pure_python      | 452 us                                                 | 281 us: 1.61x faster                                                     |
| hexiom                  | 9.43 ms                                                | 5.96 ms: 1.58x faster                                                    |
| spectral_norm           | 150 ms                                                 | 95.1 ms: 1.57x faster                                                    |
| chaos                   | 106 ms                                                 | 67.3 ms: 1.57x faster                                                    |
| deepcopy_memo           | 51.7 us                                                | 33.2 us: 1.56x faster                                                    |
| mako                    | 14.7 ms                                                | 9.42 ms: 1.55x faster                                                    |
| crypto_pyaes            | 117 ms                                                 | 75.5 ms: 1.55x faster                                                    |
| scimark_lu              | 161 ms                                                 | 105 ms: 1.53x faster                                                     |
| nbody                   | 144 ms                                                 | 94.1 ms: 1.53x faster                                                    |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                     |
| float                   | 109 ms                                                 | 72.0 ms: 1.51x faster                                                    |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.50x faster                                                    |
| chameleon               | 9.17 ms                                                | 6.26 ms: 1.47x faster                                                    |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                    |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                                   |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                    |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                                    |
| django_template         | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                    |
| json_dumps              | 13.4 ms                                                | 9.39 ms: 1.43x faster                                                    |
| pprint_safe_repr        | 953 ms                                                 | 669 ms: 1.42x faster                                                     |
| logging_simple          | 8.10 us                                                | 5.72 us: 1.42x faster                                                    |
| pycparser               | 1.53 sec                                               | 1.08 sec: 1.41x faster                                                   |
| logging_format          | 8.85 us                                                | 6.26 us: 1.41x faster                                                    |
| unpack_sequence         | 59.4 ns                                                | 42.1 ns: 1.41x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                                    |
| thrift                  | 1.03 ms                                                | 754 us: 1.37x faster                                                     |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                                    |
| genshi_xml              | 63.7 ms                                                | 46.9 ms: 1.36x faster                                                    |
| async_tree_memoization  | 855 ms                                                 | 629 ms: 1.36x faster                                                     |
| scimark_fft             | 421 ms                                                 | 310 ms: 1.36x faster                                                     |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                   |
| deepcopy                | 438 us                                                 | 323 us: 1.35x faster                                                     |
| async_tree_none         | 711 ms                                                 | 533 ms: 1.33x faster                                                     |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                     |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.31x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.30x faster                                                    |
| sqlglot_optimize        | 65.2 ms                                                | 50.3 ms: 1.30x faster                                                    |
| fannkuch                | 488 ms                                                 | 377 ms: 1.29x faster                                                     |
| nqueens                 | 100 ms                                                 | 77.4 ms: 1.29x faster                                                    |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                                     |
| coroutines              | 31.6 ms                                                | 25.3 ms: 1.25x faster                                                    |
| xml_etree_generate      | 93.8 ms                                                | 76.2 ms: 1.23x faster                                                    |
| async_generators        | 426 ms                                                 | 348 ms: 1.22x faster                                                     |
| bench_thread_pool       | 946 us                                                 | 777 us: 1.22x faster                                                     |
| dulwich_log             | 75.8 ms                                                | 62.3 ms: 1.22x faster                                                    |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                    |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                                    |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.18x faster                                                    |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                     |
| pickle_list             | 4.72 us                                                | 4.10 us: 1.15x faster                                                    |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                                     |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                                    |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                                    |
| djangocms               | 36.9 us                                                | 32.7 us: 1.13x faster                                                    |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                                     |
| json                    | 5.35 ms                                                | 4.81 ms: 1.11x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                                     |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                     |
| unpickle                | 14.2 us                                                | 13.0 us: 1.08x faster                                                    |
| mdp                     | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                   |
| telco                   | 6.73 ms                                                | 6.41 ms: 1.05x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                                     |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                     |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                                    |
| generators              | 76.4 ms                                                | 77.0 ms: 1.01x slower                                                    |
| unpickle_list           | 4.92 us                                                | 5.09 us: 1.04x slower                                                    |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                     |
| python_startup_no_site  | 5.78 ms                                                | 6.09 ms: 1.05x slower                                                    |
| regex_effbot            | 3.19 ms                                                | 3.50 ms: 1.10x slower                                                    |
| pickle_dict             | 27.6 us                                                | 30.9 us: 1.12x slower                                                    |
| coverage                | 74.7 ms                                                | 101 ms: 1.35x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221217-3.12.0a3+-ba16621/bm-20221217-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-ba16621.json: mypy
