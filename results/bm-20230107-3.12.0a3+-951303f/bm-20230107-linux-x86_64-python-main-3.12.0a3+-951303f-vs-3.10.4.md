
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 951303f
- commit date: 2023-01-07
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 255 ms: 1.32x faster                                   |
| chameleon      | 9.17 ms                                                | 6.41 ms: 1.43x faster                                  |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 109 ms                                                 | 72.8 ms: 1.50x faster                                  |
| nbody          | 144 ms                                                 | 96.7 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 20.8 ms: 1.20x faster                                  |
| regex_dna      | 214 ms                                                 | 189 ms: 1.13x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.17 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                   |
| unpickle_pure_python | 302 us                                                 | 210 us: 1.44x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.40x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 78.2 ms: 1.20x faster                                  |
| pickle_list          | 4.72 us                                                | 4.14 us: 1.14x faster                                  |
| json_loads           | 28.7 us                                                | 26.1 us: 1.10x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                   |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.06x faster                                   |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.5 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.51 ms: 1.66x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.09 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.54 ms: 1.54x faster                                  |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                  |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                  |
| genshi_xml      | 63.7 ms                                                | 47.4 ms: 1.34x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.25 ms: 2.24x faster                                  |
| logging_silent          | 176 ns                                                 | 94.1 ns: 1.88x faster                                  |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                   |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                  |
| pyflate                 | 676 ms                                                 | 402 ms: 1.68x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 64.6 ms: 1.68x faster                                  |
| python_startup          | 14.1 ms                                                | 8.51 ms: 1.66x faster                                  |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                   |
| raytrace                | 467 ms                                                 | 282 ms: 1.65x faster                                   |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                   |
| hexiom                  | 9.43 ms                                                | 6.06 ms: 1.56x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 33.6 us: 1.54x faster                                  |
| mako                    | 14.7 ms                                                | 9.54 ms: 1.54x faster                                  |
| spectral_norm           | 150 ms                                                 | 98.6 ms: 1.52x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 77.2 ms: 1.51x faster                                  |
| chaos                   | 106 ms                                                 | 70.2 ms: 1.50x faster                                  |
| float                   | 109 ms                                                 | 72.8 ms: 1.50x faster                                  |
| nbody                   | 144 ms                                                 | 96.7 ms: 1.49x faster                                  |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.48x faster                                   |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                  |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 210 us: 1.44x faster                                   |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                  |
| chameleon               | 9.17 ms                                                | 6.41 ms: 1.43x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                 |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                  |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                  |
| logging_simple          | 8.10 us                                                | 5.77 us: 1.40x faster                                  |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 42.4 ns: 1.40x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 681 ms: 1.40x faster                                   |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.40x faster                                  |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| thrift                  | 1.03 ms                                                | 757 us: 1.37x faster                                   |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.35x faster                                 |
| genshi_xml              | 63.7 ms                                                | 47.4 ms: 1.34x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.33x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.11 ms: 1.33x faster                                  |
| async_tree_none         | 711 ms                                                 | 536 ms: 1.33x faster                                   |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                   |
| 2to3                    | 335 ms                                                 | 255 ms: 1.32x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.30x faster                                  |
| scimark_fft             | 421 ms                                                 | 325 ms: 1.30x faster                                   |
| fannkuch                | 488 ms                                                 | 376 ms: 1.30x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 672 ms: 1.27x faster                                   |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                 |
| sqlglot_optimize        | 65.2 ms                                                | 51.7 ms: 1.26x faster                                  |
| coroutines              | 31.6 ms                                                | 25.2 ms: 1.25x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                   |
| sqlglot_normalize       | 134 ms                                                 | 107 ms: 1.25x faster                                   |
| nqueens                 | 100 ms                                                 | 81.0 ms: 1.24x faster                                  |
| bench_thread_pool       | 946 us                                                 | 781 us: 1.21x faster                                   |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.21x faster                                  |
| regex_v8                | 25.0 ms                                                | 20.8 ms: 1.20x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 78.2 ms: 1.20x faster                                  |
| async_generators        | 426 ms                                                 | 356 ms: 1.20x faster                                   |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 462 ms: 1.16x faster                                   |
| djangocms               | 36.9 us                                                | 32.2 us: 1.15x faster                                  |
| pickle_list             | 4.72 us                                                | 4.14 us: 1.14x faster                                  |
| sympy_str               | 325 ms                                                 | 285 ms: 1.14x faster                                   |
| regex_dna               | 214 ms                                                 | 189 ms: 1.13x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.12x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                   |
| json_loads              | 28.7 us                                                | 26.1 us: 1.10x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                   |
| json                    | 5.35 ms                                                | 4.92 ms: 1.09x faster                                  |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                   |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.06x faster                                   |
| telco                   | 6.73 ms                                                | 6.36 ms: 1.06x faster                                  |
| mdp                     | 2.74 sec                                               | 2.63 sec: 1.04x faster                                 |
| regex_effbot            | 3.19 ms                                                | 3.17 ms: 1.01x faster                                  |
| generators              | 76.4 ms                                                | 76.2 ms: 1.00x faster                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.09 ms: 1.05x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.5 us: 1.14x slower                                  |
| coverage                | 74.7 ms                                                | 99.3 ms: 1.33x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230107-3.12.0a3+-951303f/bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f.json: mypy
