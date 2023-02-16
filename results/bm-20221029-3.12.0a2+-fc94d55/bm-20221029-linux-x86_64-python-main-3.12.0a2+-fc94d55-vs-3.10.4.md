
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: fc94d55
- commit date: 2022-10-29
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.37 ms: 1.44x faster                                  |
| html5lib       | 85.9 ms                                                | 59.5 ms: 1.44x faster                                  |
| tornado_http   | 128 ms                                                 | 93.1 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 109 ms                                                 | 72.9 ms: 1.49x faster                                  |
| nbody          | 144 ms                                                 | 98.1 ms: 1.47x faster                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.9 ms: 1.09x faster                                  |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.69 ms: 1.16x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                   |
| unpickle_pure_python | 302 us                                                 | 205 us: 1.47x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.31 ms: 1.44x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.1 ms: 1.40x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.1 ms: 1.23x faster                                  |
| json_loads           | 28.7 us                                                | 23.5 us: 1.22x faster                                  |
| pickle_list          | 4.72 us                                                | 4.16 us: 1.13x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| unpickle             | 14.2 us                                                | 12.9 us: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle_list        | 4.92 us                                                | 4.97 us: 1.01x slower                                  |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.6 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.37 ms: 1.68x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.08 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.72 ms: 1.51x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.1 ms: 1.45x faster                                  |
| django_template | 46.3 ms                                                | 32.0 ms: 1.45x faster                                  |
| genshi_xml      | 63.7 ms                                                | 49.2 ms: 1.29x faster                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.30 ms: 2.20x faster                                  |
| logging_silent          | 176 ns                                                 | 94.4 ns: 1.87x faster                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                   |
| richards                | 75.2 ms                                                | 43.4 ms: 1.73x faster                                  |
| pyflate                 | 676 ms                                                 | 399 ms: 1.69x faster                                   |
| python_startup          | 14.1 ms                                                | 8.37 ms: 1.68x faster                                  |
| scimark_monte_carlo     | 109 ms                                                 | 65.6 ms: 1.65x faster                                  |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                   |
| raytrace                | 467 ms                                                 | 285 ms: 1.64x faster                                   |
| spectral_norm           | 150 ms                                                 | 94.1 ms: 1.59x faster                                  |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                   |
| chaos                   | 106 ms                                                 | 67.4 ms: 1.57x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 74.7 ms: 1.56x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.34 ms: 1.53x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.22 ms: 1.51x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.3 us: 1.51x faster                                  |
| mako                    | 14.7 ms                                                | 9.72 ms: 1.51x faster                                  |
| float                   | 109 ms                                                 | 72.9 ms: 1.49x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.63 ms: 1.49x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 205 us: 1.47x faster                                   |
| nbody                   | 144 ms                                                 | 98.1 ms: 1.47x faster                                  |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                   |
| genshi_text             | 30.6 ms                                                | 21.1 ms: 1.45x faster                                  |
| django_template         | 46.3 ms                                                | 32.0 ms: 1.45x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                 |
| json_dumps              | 13.4 ms                                                | 9.31 ms: 1.44x faster                                  |
| html5lib                | 85.9 ms                                                | 59.5 ms: 1.44x faster                                  |
| chameleon               | 9.17 ms                                                | 6.37 ms: 1.44x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 670 ms: 1.42x faster                                   |
| thrift                  | 1.03 ms                                                | 736 us: 1.41x faster                                   |
| xml_etree_process       | 74.5 ms                                                | 53.1 ms: 1.40x faster                                  |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                  |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                 |
| logging_format          | 8.85 us                                                | 6.41 us: 1.38x faster                                  |
| tornado_http            | 128 ms                                                 | 93.1 ms: 1.38x faster                                  |
| regex_compile           | 177 ms                                                 | 130 ms: 1.37x faster                                   |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                 |
| async_tree_memoization  | 855 ms                                                 | 638 ms: 1.34x faster                                   |
| deepcopy                | 438 us                                                 | 328 us: 1.33x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                  |
| async_tree_none         | 711 ms                                                 | 536 ms: 1.33x faster                                   |
| scimark_fft             | 421 ms                                                 | 318 ms: 1.32x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                  |
| fannkuch                | 488 ms                                                 | 373 ms: 1.31x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                  |
| coroutines              | 31.6 ms                                                | 24.4 ms: 1.30x faster                                  |
| genshi_xml              | 63.7 ms                                                | 49.2 ms: 1.29x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 46.0 ns: 1.29x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 737 ms: 1.29x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.27 ms: 1.28x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 51.5 ms: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 80.7 ms: 1.24x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.1 ms: 1.23x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.6 ms: 1.23x faster                                  |
| json_loads              | 28.7 us                                                | 23.5 us: 1.22x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                   |
| pylint                  | 532 ms                                                 | 459 ms: 1.16x faster                                   |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                   |
| json                    | 5.35 ms                                                | 4.67 ms: 1.14x faster                                  |
| pickle_list             | 4.72 us                                                | 4.16 us: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                  |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.64 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.9 ms: 1.09x faster                                  |
| unpickle                | 14.2 us                                                | 12.9 us: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| mdp                     | 2.74 sec                                               | 2.54 sec: 1.08x faster                                 |
| telco                   | 6.73 ms                                                | 6.31 ms: 1.07x faster                                  |
| generators              | 76.4 ms                                                | 72.6 ms: 1.05x faster                                  |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                   |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                   |
| unpickle_list           | 4.92 us                                                | 4.97 us: 1.01x slower                                  |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.08 ms: 1.05x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.6 us: 1.15x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.69 ms: 1.16x slower                                  |
| coverage                | 74.7 ms                                                | 97.3 ms: 1.30x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221029-3.12.0a2+-fc94d55/bm-20221029-linux-x86_64-python-main-3.12.0a2+-fc94d55.json: mypy
