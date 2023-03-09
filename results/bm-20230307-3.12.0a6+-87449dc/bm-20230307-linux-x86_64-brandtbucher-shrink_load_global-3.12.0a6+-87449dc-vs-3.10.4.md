
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: 87449dc
- commit date: 2023-03-07
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.43 ms: 1.43x faster                                                      |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                     |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                      |
| tornado_http   | 128 ms                                                 | 95.2 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 91.6 ms: 1.57x faster                                                      |
| float          | 109 ms                                                 | 74.3 ms: 1.47x faster                                                      |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                       |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                      |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                                       |
| regex_effbot   | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 290 us: 1.56x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 201 us: 1.50x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.49 ms: 1.42x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 55.6 ms: 1.34x faster                                                      |
| json_loads           | 28.7 us                                                | 24.2 us: 1.18x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 80.9 ms: 1.16x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.18 us: 1.13x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 99.3 ms: 1.12x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                                      |
| pickle               | 10.2 us                                                | 10.5 us: 1.03x slower                                                      |
| unpickle_list        | 4.92 us                                                | 5.13 us: 1.04x slower                                                      |
| pickle_dict          | 27.6 us                                                | 31.2 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.99 ms: 1.57x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.52 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.1 ms: 1.46x faster                                                      |
| genshi_text     | 30.6 ms                                                | 21.9 ms: 1.40x faster                                                      |
| django_template | 46.3 ms                                                | 33.6 ms: 1.38x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 48.9 ms: 1.30x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.9 ms: 2.47x faster                                                      |
| deltablue               | 7.28 ms                                                | 3.23 ms: 2.25x faster                                                      |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                       |
| logging_silent          | 176 ns                                                 | 96.4 ns: 1.83x faster                                                      |
| asyncio_tcp             | 914 ms                                                 | 508 ms: 1.80x faster                                                       |
| richards                | 75.2 ms                                                | 43.4 ms: 1.73x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                 | 66.8 ms: 1.62x faster                                                      |
| pyflate                 | 676 ms                                                 | 418 ms: 1.62x faster                                                       |
| raytrace                | 467 ms                                                 | 289 ms: 1.62x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 72.8 ms: 1.60x faster                                                      |
| go                      | 226 ms                                                 | 142 ms: 1.59x faster                                                       |
| nbody                   | 144 ms                                                 | 91.6 ms: 1.57x faster                                                      |
| spectral_norm           | 150 ms                                                 | 95.2 ms: 1.57x faster                                                      |
| python_startup          | 14.1 ms                                                | 8.99 ms: 1.57x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 290 us: 1.56x faster                                                       |
| chaos                   | 106 ms                                                 | 68.0 ms: 1.55x faster                                                      |
| hexiom                  | 9.43 ms                                                | 6.20 ms: 1.52x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 201 us: 1.50x faster                                                       |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                                      |
| float                   | 109 ms                                                 | 74.3 ms: 1.47x faster                                                      |
| mako                    | 14.7 ms                                                | 10.1 ms: 1.46x faster                                                      |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.45x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.43 ms: 1.43x faster                                                      |
| json_dumps              | 13.4 ms                                                | 9.49 ms: 1.42x faster                                                      |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                      |
| genshi_text             | 30.6 ms                                                | 21.9 ms: 1.40x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.47 ms: 1.39x faster                                                      |
| pprint_pformat          | 1.98 sec                                               | 1.43 sec: 1.39x faster                                                     |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.38x faster                                                     |
| django_template         | 46.3 ms                                                | 33.6 ms: 1.38x faster                                                      |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                     |
| logging_simple          | 8.10 us                                                | 5.88 us: 1.38x faster                                                      |
| sqlglot_transpile       | 2.43 ms                                                | 1.77 ms: 1.37x faster                                                      |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.36x faster                                                       |
| pprint_safe_repr        | 953 ms                                                 | 700 ms: 1.36x faster                                                       |
| coroutines              | 31.6 ms                                                | 23.3 ms: 1.36x faster                                                      |
| async_tree_none         | 711 ms                                                 | 528 ms: 1.35x faster                                                       |
| tornado_http            | 128 ms                                                 | 95.2 ms: 1.35x faster                                                      |
| logging_format          | 8.85 us                                                | 6.58 us: 1.35x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 55.6 ms: 1.34x faster                                                      |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                       |
| fannkuch                | 488 ms                                                 | 367 ms: 1.33x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.32x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                      |
| thrift                  | 1.03 ms                                                | 784 us: 1.32x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 45.2 ns: 1.31x faster                                                      |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                       |
| async_tree_memoization  | 855 ms                                                 | 656 ms: 1.30x faster                                                       |
| genshi_xml              | 63.7 ms                                                | 48.9 ms: 1.30x faster                                                      |
| deepcopy                | 438 us                                                 | 337 us: 1.30x faster                                                       |
| mypy2                   | 430 ms                                                 | 334 ms: 1.29x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 748 ms: 1.27x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                                      |
| deepcopy_reduce         | 3.79 us                                                | 3.04 us: 1.25x faster                                                      |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.50 ms: 1.21x faster                                                      |
| nqueens                 | 100 ms                                                 | 83.0 ms: 1.21x faster                                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 794 us: 1.19x faster                                                       |
| dulwich_log             | 75.8 ms                                                | 63.7 ms: 1.19x faster                                                      |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.1 ms: 1.18x faster                                                      |
| json_loads              | 28.7 us                                                | 24.2 us: 1.18x faster                                                      |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                      |
| xml_etree_generate      | 93.8 ms                                                | 80.9 ms: 1.16x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 20.7 ms: 1.16x faster                                                      |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                      |
| sympy_expand            | 534 ms                                                 | 466 ms: 1.15x faster                                                       |
| sympy_str               | 325 ms                                                 | 286 ms: 1.13x faster                                                       |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                      |
| pickle_list             | 4.72 us                                                | 4.18 us: 1.13x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 99.3 ms: 1.12x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                      |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.11x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.47 sec: 1.11x faster                                                     |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                                       |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                       |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                                       |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                                      |
| telco                   | 6.73 ms                                                | 6.50 ms: 1.04x faster                                                      |
| async_generators        | 426 ms                                                 | 415 ms: 1.03x faster                                                       |
| pickle                  | 10.2 us                                                | 10.5 us: 1.03x slower                                                      |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                       |
| unpickle_list           | 4.92 us                                                | 5.13 us: 1.04x slower                                                      |
| gc_traversal            | 3.53 ms                                                | 3.81 ms: 1.08x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.54 ms: 1.11x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.52 ms: 1.13x slower                                                      |
| pickle_dict             | 27.6 us                                                | 31.2 us: 1.13x slower                                                      |
| dask                    | 436 ms                                                 | 512 ms: 1.17x slower                                                       |
| coverage                | 74.7 ms                                                | 94.4 ms: 1.26x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230307-3.12.0a6+-87449dc/bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc.json: comprehensions
