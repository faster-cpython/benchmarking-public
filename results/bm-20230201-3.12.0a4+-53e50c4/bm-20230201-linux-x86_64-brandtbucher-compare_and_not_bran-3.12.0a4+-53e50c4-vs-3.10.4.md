
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: 53e50c4
- commit date: 2023-02-01
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 254 ms: 1.31x faster                                                         |
| chameleon      | 8.86 ms                                                | 6.44 ms: 1.37x faster                                                        |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                       |
| html5lib       | 85.8 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.1 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.6 ms: 1.48x faster                                                        |
| nbody          | 136 ms                                                 | 93.7 ms: 1.45x faster                                                        |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.33x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.12x faster                                                        |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                         |
| regex_effbot   | 3.21 ms                                                | 3.52 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 288 us: 1.57x faster                                                         |
| unpickle_pure_python | 297 us                                                 | 202 us: 1.46x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.62 ms: 1.40x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                        |
| xml_etree_generate   | 93.3 ms                                                | 77.7 ms: 1.20x faster                                                        |
| json_loads           | 28.9 us                                                | 24.0 us: 1.20x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| unpickle             | 14.3 us                                                | 13.0 us: 1.10x faster                                                        |
| pickle_list          | 4.50 us                                                | 4.10 us: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                 | 105 ms: 1.05x faster                                                         |
| unpickle_list        | 4.99 us                                                | 4.96 us: 1.01x faster                                                        |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| pickle_dict          | 28.3 us                                                | 30.7 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.89 ms: 1.57x faster                                                        |
| python_startup_no_site | 5.76 ms                                                | 6.44 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                        |
| mako            | 14.3 ms                                                | 9.69 ms: 1.47x faster                                                        |
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                        |
| genshi_xml      | 63.6 ms                                                | 46.6 ms: 1.36x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.21 ms: 2.30x faster                                                        |
| logging_silent          | 173 ns                                                 | 93.7 ns: 1.85x faster                                                        |
| scimark_sor             | 193 ms                                                 | 108 ms: 1.78x faster                                                         |
| richards                | 71.4 ms                                                | 42.1 ms: 1.70x faster                                                        |
| pyflate                 | 675 ms                                                 | 400 ms: 1.69x faster                                                         |
| go                      | 226 ms                                                 | 137 ms: 1.66x faster                                                         |
| raytrace                | 461 ms                                                 | 281 ms: 1.64x faster                                                         |
| scimark_monte_carlo     | 105 ms                                                 | 65.0 ms: 1.61x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 72.9 ms: 1.61x faster                                                        |
| chaos                   | 104 ms                                                 | 65.0 ms: 1.60x faster                                                        |
| hexiom                  | 9.42 ms                                                | 5.89 ms: 1.60x faster                                                        |
| pickle_pure_python      | 453 us                                                 | 288 us: 1.57x faster                                                         |
| spectral_norm           | 148 ms                                                 | 94.5 ms: 1.57x faster                                                        |
| python_startup          | 13.9 ms                                                | 8.89 ms: 1.57x faster                                                        |
| scimark_lu              | 158 ms                                                 | 105 ms: 1.51x faster                                                         |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                                        |
| float                   | 108 ms                                                 | 72.6 ms: 1.48x faster                                                        |
| mako                    | 14.3 ms                                                | 9.69 ms: 1.47x faster                                                        |
| unpickle_pure_python    | 297 us                                                 | 202 us: 1.46x faster                                                         |
| nbody                   | 136 ms                                                 | 93.7 ms: 1.45x faster                                                        |
| deepcopy_memo           | 50.0 us                                                | 34.7 us: 1.44x faster                                                        |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.43x faster                                                        |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                       |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                                        |
| json_dumps              | 13.5 ms                                                | 9.62 ms: 1.40x faster                                                        |
| logging_format          | 8.92 us                                                | 6.38 us: 1.40x faster                                                        |
| html5lib                | 85.8 ms                                                | 61.3 ms: 1.40x faster                                                        |
| pprint_safe_repr        | 943 ms                                                 | 675 ms: 1.40x faster                                                         |
| logging_simple          | 8.06 us                                                | 5.78 us: 1.39x faster                                                        |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                        |
| chameleon               | 8.86 ms                                                | 6.44 ms: 1.37x faster                                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.00 ms: 1.37x faster                                                        |
| scimark_fft             | 414 ms                                                 | 302 ms: 1.37x faster                                                         |
| unpack_sequence         | 59.5 ns                                                | 43.6 ns: 1.36x faster                                                        |
| tornado_http            | 128 ms                                                 | 94.1 ms: 1.36x faster                                                        |
| genshi_xml              | 63.6 ms                                                | 46.6 ms: 1.36x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 995 us: 1.34x faster                                                         |
| async_tree_none         | 713 ms                                                 | 530 ms: 1.34x faster                                                         |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                       |
| regex_compile           | 174 ms                                                 | 130 ms: 1.33x faster                                                         |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.32x faster                                                       |
| fannkuch                | 477 ms                                                 | 364 ms: 1.31x faster                                                         |
| 2to3                    | 332 ms                                                 | 254 ms: 1.31x faster                                                         |
| deepcopy                | 429 us                                                 | 329 us: 1.31x faster                                                         |
| async_tree_memoization  | 854 ms                                                 | 666 ms: 1.28x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                        |
| deepcopy_reduce         | 3.75 us                                                | 2.93 us: 1.28x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                         |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                         |
| nqueens                 | 99.3 ms                                                | 79.0 ms: 1.26x faster                                                        |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 759 ms: 1.25x faster                                                         |
| coroutines              | 31.7 ms                                                | 25.5 ms: 1.24x faster                                                        |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                                        |
| async_generators        | 428 ms                                                 | 353 ms: 1.21x faster                                                         |
| dulwich_log             | 75.5 ms                                                | 62.8 ms: 1.20x faster                                                        |
| xml_etree_generate      | 93.3 ms                                                | 77.7 ms: 1.20x faster                                                        |
| json_loads              | 28.9 us                                                | 24.0 us: 1.20x faster                                                        |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                         |
| bench_thread_pool       | 943 us                                                 | 787 us: 1.20x faster                                                         |
| sympy_expand            | 537 ms                                                 | 454 ms: 1.18x faster                                                         |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                         |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                                        |
| sqlite_synth            | 2.90 us                                                | 2.57 us: 1.13x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.12x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| unpickle                | 14.3 us                                                | 13.0 us: 1.10x faster                                                        |
| pickle_list             | 4.50 us                                                | 4.10 us: 1.10x faster                                                        |
| mdp                     | 2.82 sec                                               | 2.58 sec: 1.10x faster                                                       |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                         |
| xml_etree_iterparse     | 110 ms                                                 | 105 ms: 1.05x faster                                                         |
| telco                   | 6.68 ms                                                | 6.40 ms: 1.04x faster                                                        |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                         |
| unpickle_list           | 4.99 us                                                | 4.96 us: 1.01x faster                                                        |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                         |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                        |
| generators              | 75.8 ms                                                | 76.5 ms: 1.01x slower                                                        |
| pickle_dict             | 28.3 us                                                | 30.7 us: 1.09x slower                                                        |
| regex_effbot            | 3.21 ms                                                | 3.52 ms: 1.10x slower                                                        |
| python_startup_no_site  | 5.76 ms                                                | 6.44 ms: 1.12x slower                                                        |
| coverage                | 75.3 ms                                                | 96.1 ms: 1.28x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230201-3.12.0a4+-53e50c4/bm-20230201-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a4+-53e50c4.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
