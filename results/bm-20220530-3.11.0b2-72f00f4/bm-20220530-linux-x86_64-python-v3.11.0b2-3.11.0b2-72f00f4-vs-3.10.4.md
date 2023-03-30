
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b2
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 256 ms: 1.31x faster                                       |
| chameleon      | 9.13 ms                                                             | 6.62 ms: 1.38x faster                                      |
| docutils       | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                     |
| html5lib       | 86.4 ms                                                             | 63.7 ms: 1.35x faster                                      |
| tornado_http   | 129 ms                                                              | 94.9 ms: 1.36x faster                                      |
| Geometric mean | (ref)                                                               | 1.33x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 146 ms                                                              | 92.0 ms: 1.59x faster                                      |
| float          | 110 ms                                                              | 74.4 ms: 1.48x faster                                      |
| pidigits       | 190 ms                                                              | 199 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                               | 1.31x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 138 ms: 1.29x faster                                       |
| regex_v8       | 24.9 ms                                                             | 22.0 ms: 1.14x faster                                      |
| regex_dna      | 213 ms                                                              | 196 ms: 1.09x faster                                       |
| regex_effbot   | 3.22 ms                                                             | 3.11 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                               | 1.13x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 305 us: 1.50x faster                                       |
| xml_etree_process    | 74.8 ms                                                             | 53.4 ms: 1.40x faster                                      |
| unpickle_pure_python | 300 us                                                              | 227 us: 1.32x faster                                       |
| xml_etree_generate   | 94.9 ms                                                             | 76.1 ms: 1.25x faster                                      |
| json_loads           | 29.3 us                                                             | 25.0 us: 1.17x faster                                      |
| unpickle             | 15.0 us                                                             | 13.3 us: 1.12x faster                                      |
| pickle_list          | 4.73 us                                                             | 4.30 us: 1.10x faster                                      |
| pickle               | 10.2 us                                                             | 9.44 us: 1.08x faster                                      |
| json_dumps           | 13.7 ms                                                             | 12.8 ms: 1.07x faster                                      |
| xml_etree_iterparse  | 111 ms                                                              | 105 ms: 1.06x faster                                       |
| pickle_dict          | 27.8 us                                                             | 26.4 us: 1.05x faster                                      |
| xml_etree_parse      | 164 ms                                                              | 159 ms: 1.03x faster                                       |
| unpickle_list        | 4.94 us                                                             | 5.00 us: 1.01x slower                                      |
| Geometric mean       | (ref)                                                               | 1.16x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.49 ms: 1.66x faster                                      |
| python_startup_no_site | 5.80 ms                                                             | 5.99 ms: 1.03x slower                                      |
| Geometric mean         | (ref)                                                               | 1.27x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.96 ms: 1.48x faster                                      |
| genshi_text     | 30.4 ms                                                             | 21.5 ms: 1.41x faster                                      |
| django_template | 45.8 ms                                                             | 32.6 ms: 1.41x faster                                      |
| genshi_xml      | 64.3 ms                                                             | 52.4 ms: 1.23x faster                                      |
| Geometric mean  | (ref)                                                               | 1.38x faster                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.84 ms: 1.90x faster                                      |
| scimark_sor             | 198 ms                                                              | 115 ms: 1.72x faster                                       |
| richards                | 74.2 ms                                                             | 44.5 ms: 1.67x faster                                      |
| python_startup          | 14.1 ms                                                             | 8.49 ms: 1.66x faster                                      |
| scimark_monte_carlo     | 109 ms                                                              | 66.0 ms: 1.64x faster                                      |
| logging_silent          | 169 ns                                                              | 103 ns: 1.64x faster                                       |
| raytrace                | 470 ms                                                              | 287 ms: 1.64x faster                                       |
| go                      | 226 ms                                                              | 139 ms: 1.63x faster                                       |
| pyflate                 | 671 ms                                                              | 413 ms: 1.62x faster                                       |
| nbody                   | 146 ms                                                              | 92.0 ms: 1.59x faster                                      |
| chaos                   | 106 ms                                                              | 67.3 ms: 1.57x faster                                      |
| crypto_pyaes            | 117 ms                                                              | 74.8 ms: 1.56x faster                                      |
| spectral_norm           | 150 ms                                                              | 97.3 ms: 1.54x faster                                      |
| hexiom                  | 9.50 ms                                                             | 6.27 ms: 1.52x faster                                      |
| pickle_pure_python      | 457 us                                                              | 305 us: 1.50x faster                                       |
| mako                    | 14.7 ms                                                             | 9.96 ms: 1.48x faster                                      |
| float                   | 110 ms                                                              | 74.4 ms: 1.48x faster                                      |
| scimark_lu              | 160 ms                                                              | 109 ms: 1.47x faster                                       |
| deepcopy_memo           | 51.8 us                                                             | 35.9 us: 1.44x faster                                      |
| logging_simple          | 8.21 us                                                             | 5.74 us: 1.43x faster                                      |
| logging_format          | 9.07 us                                                             | 6.34 us: 1.43x faster                                      |
| unpack_sequence         | 65.6 ns                                                             | 46.2 ns: 1.42x faster                                      |
| genshi_text             | 30.4 ms                                                             | 21.5 ms: 1.41x faster                                      |
| django_template         | 45.8 ms                                                             | 32.6 ms: 1.41x faster                                      |
| xml_etree_process       | 74.8 ms                                                             | 53.4 ms: 1.40x faster                                      |
| thrift                  | 1.04 ms                                                             | 750 us: 1.38x faster                                       |
| chameleon               | 9.13 ms                                                             | 6.62 ms: 1.38x faster                                      |
| pprint_pformat          | 1.98 sec                                                            | 1.45 sec: 1.37x faster                                     |
| pprint_safe_repr        | 953 ms                                                              | 699 ms: 1.36x faster                                       |
| async_tree_io           | 1.78 sec                                                            | 1.31 sec: 1.36x faster                                     |
| tornado_http            | 129 ms                                                              | 94.9 ms: 1.36x faster                                      |
| async_tree_memoization  | 853 ms                                                              | 628 ms: 1.36x faster                                       |
| async_tree_none         | 713 ms                                                              | 526 ms: 1.36x faster                                       |
| html5lib                | 86.4 ms                                                             | 63.7 ms: 1.35x faster                                      |
| pycparser               | 1.53 sec                                                            | 1.14 sec: 1.34x faster                                     |
| unpickle_pure_python    | 300 us                                                              | 227 us: 1.32x faster                                       |
| 2to3                    | 336 ms                                                              | 256 ms: 1.31x faster                                       |
| scimark_fft             | 425 ms                                                              | 329 ms: 1.29x faster                                       |
| deepcopy                | 438 us                                                              | 340 us: 1.29x faster                                       |
| regex_compile           | 177 ms                                                              | 138 ms: 1.29x faster                                       |
| aiohttp                 | 1.35 ms                                                             | 1.06 ms: 1.28x faster                                      |
| gunicorn                | 1.43 ms                                                             | 1.13 ms: 1.27x faster                                      |
| async_tree_cpu_io_mixed | 944 ms                                                              | 743 ms: 1.27x faster                                       |
| deepcopy_reduce         | 3.80 us                                                             | 3.03 us: 1.25x faster                                      |
| docutils                | 3.19 sec                                                            | 2.56 sec: 1.25x faster                                     |
| xml_etree_generate      | 94.9 ms                                                             | 76.1 ms: 1.25x faster                                      |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.51 ms: 1.24x faster                                      |
| coroutines              | 31.8 ms                                                             | 25.7 ms: 1.24x faster                                      |
| genshi_xml              | 64.3 ms                                                             | 52.4 ms: 1.23x faster                                      |
| sqlglot_normalize       | 135 ms                                                              | 110 ms: 1.22x faster                                       |
| sqlalchemy_declarative  | 166 ms                                                              | 137 ms: 1.22x faster                                       |
| sqlglot_optimize        | 65.3 ms                                                             | 53.9 ms: 1.21x faster                                      |
| dulwich_log             | 76.3 ms                                                             | 63.1 ms: 1.21x faster                                      |
| fannkuch                | 485 ms                                                              | 403 ms: 1.20x faster                                       |
| sqlglot_transpile       | 2.45 ms                                                             | 2.05 ms: 1.20x faster                                      |
| dask                    | 437 ms                                                              | 368 ms: 1.19x faster                                       |
| async_generators        | 420 ms                                                              | 354 ms: 1.19x faster                                       |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.9 ms: 1.18x faster                                      |
| sqlglot_parse           | 2.07 ms                                                             | 1.75 ms: 1.18x faster                                      |
| sqlite_synth            | 2.97 us                                                             | 2.52 us: 1.18x faster                                      |
| sympy_integrate         | 24.3 ms                                                             | 20.7 ms: 1.18x faster                                      |
| bench_thread_pool       | 954 us                                                              | 811 us: 1.18x faster                                       |
| nqueens                 | 98.8 ms                                                             | 84.2 ms: 1.17x faster                                      |
| json_loads              | 29.3 us                                                             | 25.0 us: 1.17x faster                                      |
| sympy_sum               | 185 ms                                                              | 161 ms: 1.15x faster                                       |
| json                    | 5.41 ms                                                             | 4.75 ms: 1.14x faster                                      |
| sympy_str               | 328 ms                                                              | 288 ms: 1.14x faster                                       |
| sympy_expand            | 540 ms                                                              | 475 ms: 1.14x faster                                       |
| regex_v8                | 24.9 ms                                                             | 22.0 ms: 1.14x faster                                      |
| pylint                  | 521 ms                                                              | 462 ms: 1.13x faster                                       |
| unpickle                | 15.0 us                                                             | 13.3 us: 1.12x faster                                      |
| pickle_list             | 4.73 us                                                             | 4.30 us: 1.10x faster                                      |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                       |
| pathlib                 | 19.8 ms                                                             | 18.1 ms: 1.09x faster                                      |
| create_gc_cycles        | 1.64 ms                                                             | 1.51 ms: 1.09x faster                                      |
| regex_dna               | 213 ms                                                              | 196 ms: 1.09x faster                                       |
| djangocms               | 36.3 us                                                             | 33.5 us: 1.08x faster                                      |
| pickle                  | 10.2 us                                                             | 9.44 us: 1.08x faster                                      |
| json_dumps              | 13.7 ms                                                             | 12.8 ms: 1.07x faster                                      |
| xml_etree_iterparse     | 111 ms                                                              | 105 ms: 1.06x faster                                       |
| pickle_dict             | 27.8 us                                                             | 26.4 us: 1.05x faster                                      |
| comprehensions          | 27.3 us                                                             | 26.0 us: 1.05x faster                                      |
| regex_effbot            | 3.22 ms                                                             | 3.11 ms: 1.04x faster                                      |
| asyncio_tcp             | 922 ms                                                              | 890 ms: 1.04x faster                                       |
| xml_etree_parse         | 164 ms                                                              | 159 ms: 1.03x faster                                       |
| mdp                     | 2.75 sec                                                            | 2.67 sec: 1.03x faster                                     |
| telco                   | 6.67 ms                                                             | 6.54 ms: 1.02x faster                                      |
| generators              | 75.7 ms                                                             | 74.4 ms: 1.02x faster                                      |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                      |
| unpickle_list           | 4.94 us                                                             | 5.00 us: 1.01x slower                                      |
| python_startup_no_site  | 5.80 ms                                                             | 5.99 ms: 1.03x slower                                      |
| pidigits                | 190 ms                                                              | 199 ms: 1.05x slower                                       |
| gc_traversal            | 3.53 ms                                                             | 4.21 ms: 1.19x slower                                      |
| Geometric mean          | (ref)                                                               | 1.26x faster                                               |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: coverage, flaskblogging
