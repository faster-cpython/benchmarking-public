
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache
- machine: linux-x86_64
- commit hash: 30483bd
- commit date: 2023-03-24
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 253 ms: 1.33x faster                                               |
| chameleon      | 9.13 ms                                                             | 6.54 ms: 1.40x faster                                              |
| docutils       | 3.19 sec                                                            | 2.55 sec: 1.25x faster                                             |
| html5lib       | 86.4 ms                                                             | 61.4 ms: 1.41x faster                                              |
| tornado_http   | 129 ms                                                              | 92.2 ms: 1.40x faster                                              |
| Geometric mean | (ref)                                                               | 1.36x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.6 ms: 1.66x faster                                              |
| float          | 110 ms                                                              | 73.6 ms: 1.49x faster                                              |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                               | 1.36x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 135 ms: 1.31x faster                                               |
| regex_v8       | 24.9 ms                                                             | 22.5 ms: 1.11x faster                                              |
| regex_dna      | 213 ms                                                              | 208 ms: 1.02x faster                                               |
| regex_effbot   | 3.22 ms                                                             | 3.53 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                               | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 290 us: 1.57x faster                                               |
| unpickle_pure_python | 300 us                                                              | 204 us: 1.47x faster                                               |
| json_dumps           | 13.7 ms                                                             | 9.86 ms: 1.39x faster                                              |
| xml_etree_process    | 74.8 ms                                                             | 56.4 ms: 1.33x faster                                              |
| json_loads           | 29.3 us                                                             | 24.0 us: 1.22x faster                                              |
| xml_etree_generate   | 94.9 ms                                                             | 81.4 ms: 1.17x faster                                              |
| pickle_list          | 4.73 us                                                             | 4.10 us: 1.15x faster                                              |
| unpickle             | 15.0 us                                                             | 13.3 us: 1.13x faster                                              |
| xml_etree_parse      | 164 ms                                                              | 151 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                               |
| pickle               | 10.2 us                                                             | 10.3 us: 1.01x slower                                              |
| unpickle_list        | 4.94 us                                                             | 5.12 us: 1.04x slower                                              |
| pickle_dict          | 27.8 us                                                             | 32.3 us: 1.16x slower                                              |
| Geometric mean       | (ref)                                                               | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.85 ms: 1.60x faster                                              |
| python_startup_no_site | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                               | 1.19x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.95 ms: 1.48x faster                                              |
| genshi_text     | 30.4 ms                                                             | 21.8 ms: 1.40x faster                                              |
| django_template | 45.8 ms                                                             | 33.5 ms: 1.37x faster                                              |
| genshi_xml      | 64.3 ms                                                             | 48.2 ms: 1.33x faster                                              |
| Geometric mean  | (ref)                                                               | 1.39x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230324-linux-x86_64-brandtbucher-type_cache-3.12.0a6+-30483bd |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.4 ms: 2.58x faster                                              |
| deltablue               | 7.30 ms                                                             | 3.31 ms: 2.20x faster                                              |
| scimark_sor             | 198 ms                                                              | 108 ms: 1.83x faster                                               |
| asyncio_tcp             | 922 ms                                                              | 510 ms: 1.81x faster                                               |
| logging_silent          | 169 ns                                                              | 96.6 ns: 1.75x faster                                              |
| richards                | 74.2 ms                                                             | 43.0 ms: 1.73x faster                                              |
| nbody                   | 146 ms                                                              | 87.6 ms: 1.66x faster                                              |
| spectral_norm           | 150 ms                                                              | 91.5 ms: 1.64x faster                                              |
| go                      | 226 ms                                                              | 139 ms: 1.63x faster                                               |
| raytrace                | 470 ms                                                              | 290 ms: 1.62x faster                                               |
| scimark_monte_carlo     | 109 ms                                                              | 67.4 ms: 1.61x faster                                              |
| pyflate                 | 671 ms                                                              | 418 ms: 1.60x faster                                               |
| python_startup          | 14.1 ms                                                             | 8.85 ms: 1.60x faster                                              |
| chaos                   | 106 ms                                                              | 67.0 ms: 1.58x faster                                              |
| pickle_pure_python      | 457 us                                                              | 290 us: 1.57x faster                                               |
| crypto_pyaes            | 117 ms                                                              | 74.1 ms: 1.57x faster                                              |
| hexiom                  | 9.50 ms                                                             | 6.10 ms: 1.56x faster                                              |
| deepcopy_memo           | 51.8 us                                                             | 34.2 us: 1.51x faster                                              |
| scimark_lu              | 160 ms                                                              | 106 ms: 1.51x faster                                               |
| float                   | 110 ms                                                              | 73.6 ms: 1.49x faster                                              |
| mako                    | 14.7 ms                                                             | 9.95 ms: 1.48x faster                                              |
| unpickle_pure_python    | 300 us                                                              | 204 us: 1.47x faster                                               |
| unpack_sequence         | 65.6 ns                                                             | 45.2 ns: 1.45x faster                                              |
| sqlglot_parse           | 2.07 ms                                                             | 1.45 ms: 1.43x faster                                              |
| scimark_fft             | 425 ms                                                              | 300 ms: 1.42x faster                                               |
| html5lib                | 86.4 ms                                                             | 61.4 ms: 1.41x faster                                              |
| sqlglot_transpile       | 2.45 ms                                                             | 1.75 ms: 1.40x faster                                              |
| tornado_http            | 129 ms                                                              | 92.2 ms: 1.40x faster                                              |
| chameleon               | 9.13 ms                                                             | 6.54 ms: 1.40x faster                                              |
| genshi_text             | 30.4 ms                                                             | 21.8 ms: 1.40x faster                                              |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.03 ms: 1.39x faster                                              |
| coroutines              | 31.8 ms                                                             | 22.9 ms: 1.39x faster                                              |
| json_dumps              | 13.7 ms                                                             | 9.86 ms: 1.39x faster                                              |
| logging_format          | 9.07 us                                                             | 6.54 us: 1.39x faster                                              |
| pprint_pformat          | 1.98 sec                                                            | 1.43 sec: 1.39x faster                                             |
| logging_simple          | 8.21 us                                                             | 5.94 us: 1.38x faster                                              |
| pprint_safe_repr        | 953 ms                                                              | 692 ms: 1.38x faster                                               |
| django_template         | 45.8 ms                                                             | 33.5 ms: 1.37x faster                                              |
| async_tree_io           | 1.78 sec                                                            | 1.31 sec: 1.36x faster                                             |
| async_tree_none         | 713 ms                                                              | 531 ms: 1.34x faster                                               |
| genshi_xml              | 64.3 ms                                                             | 48.2 ms: 1.33x faster                                              |
| 2to3                    | 336 ms                                                              | 253 ms: 1.33x faster                                               |
| deepcopy                | 438 us                                                              | 330 us: 1.33x faster                                               |
| xml_etree_process       | 74.8 ms                                                             | 56.4 ms: 1.33x faster                                              |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                             |
| regex_compile           | 177 ms                                                              | 135 ms: 1.31x faster                                               |
| deepcopy_reduce         | 3.80 us                                                             | 2.94 us: 1.29x faster                                              |
| thrift                  | 1.04 ms                                                             | 805 us: 1.29x faster                                               |
| mypy2                   | 432 ms                                                              | 336 ms: 1.28x faster                                               |
| fannkuch                | 485 ms                                                              | 381 ms: 1.27x faster                                               |
| async_tree_memoization  | 853 ms                                                              | 670 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed | 944 ms                                                              | 745 ms: 1.27x faster                                               |
| sqlglot_normalize       | 135 ms                                                              | 106 ms: 1.27x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                             | 51.7 ms: 1.26x faster                                              |
| docutils                | 3.19 sec                                                            | 2.55 sec: 1.25x faster                                             |
| nqueens                 | 98.8 ms                                                             | 80.9 ms: 1.22x faster                                              |
| json_loads              | 29.3 us                                                             | 24.0 us: 1.22x faster                                              |
| bench_thread_pool       | 954 us                                                              | 798 us: 1.20x faster                                               |
| sympy_integrate         | 24.3 ms                                                             | 20.4 ms: 1.19x faster                                              |
| dulwich_log             | 76.3 ms                                                             | 64.1 ms: 1.19x faster                                              |
| xml_etree_generate      | 94.9 ms                                                             | 81.4 ms: 1.17x faster                                              |
| json                    | 5.41 ms                                                             | 4.65 ms: 1.16x faster                                              |
| sympy_expand            | 540 ms                                                              | 465 ms: 1.16x faster                                               |
| pickle_list             | 4.73 us                                                             | 4.10 us: 1.15x faster                                              |
| sympy_str               | 328 ms                                                              | 285 ms: 1.15x faster                                               |
| sqlite_synth            | 2.97 us                                                             | 2.60 us: 1.14x faster                                              |
| unpickle                | 15.0 us                                                             | 13.3 us: 1.13x faster                                              |
| comprehensions          | 27.3 us                                                             | 24.3 us: 1.12x faster                                              |
| create_gc_cycles        | 1.64 ms                                                             | 1.46 ms: 1.12x faster                                              |
| regex_v8                | 24.9 ms                                                             | 22.5 ms: 1.11x faster                                              |
| sympy_sum               | 185 ms                                                              | 167 ms: 1.11x faster                                               |
| pathlib                 | 19.8 ms                                                             | 18.0 ms: 1.10x faster                                              |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                               |
| xml_etree_parse         | 164 ms                                                              | 151 ms: 1.08x faster                                               |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                               |
| telco                   | 6.67 ms                                                             | 6.46 ms: 1.03x faster                                              |
| regex_dna               | 213 ms                                                              | 208 ms: 1.02x faster                                               |
| mdp                     | 2.75 sec                                                            | 2.71 sec: 1.01x faster                                             |
| async_generators        | 420 ms                                                              | 416 ms: 1.01x faster                                               |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                               |
| pickle                  | 10.2 us                                                             | 10.3 us: 1.01x slower                                              |
| unpickle_list           | 4.94 us                                                             | 5.12 us: 1.04x slower                                              |
| gc_traversal            | 3.53 ms                                                             | 3.83 ms: 1.09x slower                                              |
| regex_effbot            | 3.22 ms                                                             | 3.53 ms: 1.10x slower                                              |
| python_startup_no_site  | 5.80 ms                                                             | 6.53 ms: 1.13x slower                                              |
| pickle_dict             | 27.8 us                                                             | 32.3 us: 1.16x slower                                              |
| dask                    | 437 ms                                                              | 516 ms: 1.18x slower                                               |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, coverage, djangocms, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
