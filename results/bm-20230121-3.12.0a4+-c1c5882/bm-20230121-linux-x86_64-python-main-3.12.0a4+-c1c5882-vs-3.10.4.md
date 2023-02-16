
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c1c5882
- commit date: 2023-01-21
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 254 ms: 1.32x faster                                   |
| chameleon      | 9.17 ms                                                | 6.32 ms: 1.45x faster                                  |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 60.8 ms: 1.41x faster                                  |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.37x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.7 ms: 1.55x faster                                  |
| float          | 109 ms                                                 | 72.0 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                  |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.65 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.53x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.39 ms: 1.43x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 78.1 ms: 1.20x faster                                  |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                  |
| pickle_list          | 4.72 us                                                | 4.01 us: 1.18x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.04x faster                                   |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 159 ms: 1.03x faster                                   |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                  |
| unpickle_list        | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| pickle_dict          | 27.6 us                                                | 30.3 us: 1.10x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.95 ms: 1.57x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.90 ms: 1.48x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.1 ms: 1.45x faster                                  |
| django_template | 46.3 ms                                                | 32.3 ms: 1.43x faster                                  |
| genshi_xml      | 63.7 ms                                                | 47.3 ms: 1.35x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.19 ms: 2.28x faster                                  |
| logging_silent          | 176 ns                                                 | 92.0 ns: 1.92x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                   |
| asyncio_tcp             | 914 ms                                                 | 502 ms: 1.82x faster                                   |
| richards                | 75.2 ms                                                | 42.9 ms: 1.75x faster                                  |
| pyflate                 | 676 ms                                                 | 398 ms: 1.70x faster                                   |
| chaos                   | 106 ms                                                 | 62.4 ms: 1.69x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 64.5 ms: 1.68x faster                                  |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                   |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                   |
| hexiom                  | 9.43 ms                                                | 5.88 ms: 1.60x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 72.8 ms: 1.60x faster                                  |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                   |
| python_startup          | 14.1 ms                                                | 8.95 ms: 1.57x faster                                  |
| spectral_norm           | 150 ms                                                 | 95.8 ms: 1.56x faster                                  |
| nbody                   | 144 ms                                                 | 92.7 ms: 1.55x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.53x faster                                   |
| deepcopy_memo           | 51.7 us                                                | 33.9 us: 1.52x faster                                  |
| float                   | 109 ms                                                 | 72.0 ms: 1.51x faster                                  |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                   |
| mako                    | 14.7 ms                                                | 9.90 ms: 1.48x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                  |
| genshi_text             | 30.6 ms                                                | 21.1 ms: 1.45x faster                                  |
| chameleon               | 9.17 ms                                                | 6.32 ms: 1.45x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                 |
| pprint_safe_repr        | 953 ms                                                 | 665 ms: 1.43x faster                                   |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.43x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.39 ms: 1.43x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 41.7 ns: 1.42x faster                                  |
| html5lib                | 85.9 ms                                                | 60.8 ms: 1.41x faster                                  |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                  |
| regex_compile           | 177 ms                                                 | 127 ms: 1.40x faster                                   |
| scimark_fft             | 421 ms                                                 | 302 ms: 1.40x faster                                   |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| logging_simple          | 8.10 us                                                | 5.84 us: 1.39x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.97 ms: 1.37x faster                                  |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.37x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                 |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                   |
| genshi_xml              | 63.7 ms                                                | 47.3 ms: 1.35x faster                                  |
| aiohttp                 | 1.34 ms                                                | 996 us: 1.35x faster                                   |
| deepcopy                | 438 us                                                 | 325 us: 1.34x faster                                   |
| fannkuch                | 488 ms                                                 | 364 ms: 1.34x faster                                   |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.34x faster                                 |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 645 ms: 1.33x faster                                   |
| 2to3                    | 335 ms                                                 | 254 ms: 1.32x faster                                   |
| nqueens                 | 100 ms                                                 | 76.0 ms: 1.32x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                  |
| coroutines              | 31.6 ms                                                | 24.6 ms: 1.29x faster                                  |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                   |
| async_generators        | 426 ms                                                 | 347 ms: 1.23x faster                                   |
| dulwich_log             | 75.8 ms                                                | 62.5 ms: 1.21x faster                                  |
| bench_thread_pool       | 946 us                                                 | 781 us: 1.21x faster                                   |
| xml_etree_generate      | 93.8 ms                                                | 78.1 ms: 1.20x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.2 ms: 1.19x faster                                  |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                  |
| sympy_expand            | 534 ms                                                 | 452 ms: 1.18x faster                                   |
| pickle_list             | 4.72 us                                                | 4.01 us: 1.18x faster                                  |
| sympy_str               | 325 ms                                                 | 281 ms: 1.16x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                  |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                  |
| json                    | 5.35 ms                                                | 4.73 ms: 1.13x faster                                  |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                  |
| mdp                     | 2.74 sec                                               | 2.46 sec: 1.12x faster                                 |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                  |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                   |
| telco                   | 6.73 ms                                                | 6.39 ms: 1.05x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.04x faster                                   |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 159 ms: 1.03x faster                                   |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                   |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                  |
| generators              | 76.4 ms                                                | 76.6 ms: 1.00x slower                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| unpickle_list           | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.88 ms: 1.10x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.3 us: 1.10x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                  |
| dask                    | 436 ms                                                 | 497 ms: 1.14x slower                                   |
| regex_effbot            | 3.19 ms                                                | 3.65 ms: 1.14x slower                                  |
| coverage                | 74.7 ms                                                | 96.0 ms: 1.28x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230121-3.12.0a4+-c1c5882/bm-20230121-linux-x86_64-python-main-3.12.0a4+-c1c5882.json: mypy
