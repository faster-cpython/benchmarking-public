
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: f58631b
- commit date: 2022-10-22
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| chameleon      | 9.17 ms                                                | 6.60 ms: 1.39x faster                                  |
| html5lib       | 85.9 ms                                                | 59.1 ms: 1.45x faster                                  |
| tornado_http   | 128 ms                                                 | 93.1 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.9 ms: 1.53x faster                                  |
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 199 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                  |
| regex_dna      | 214 ms                                                 | 209 ms: 1.02x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.66 ms: 1.15x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 289 us: 1.57x faster                                   |
| unpickle_pure_python | 302 us                                                 | 203 us: 1.49x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.49 ms: 1.42x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.1 ms: 1.40x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 75.5 ms: 1.24x faster                                  |
| json_loads           | 28.7 us                                                | 23.5 us: 1.22x faster                                  |
| pickle_list          | 4.72 us                                                | 3.96 us: 1.19x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.2 us                                                | 13.3 us: 1.07x faster                                  |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                  |
| pickle               | 10.2 us                                                | 10.3 us: 1.02x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.0 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.37 ms: 1.68x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.06 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.75 ms: 1.50x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                  |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                  |
| genshi_xml      | 63.7 ms                                                | 49.7 ms: 1.28x faster                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.30 ms: 2.20x faster                                  |
| logging_silent          | 176 ns                                                 | 90.5 ns: 1.95x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                   |
| richards                | 75.2 ms                                                | 43.5 ms: 1.73x faster                                  |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                   |
| python_startup          | 14.1 ms                                                | 8.37 ms: 1.68x faster                                  |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 66.6 ms: 1.63x faster                                  |
| raytrace                | 467 ms                                                 | 287 ms: 1.63x faster                                   |
| spectral_norm           | 150 ms                                                 | 95.1 ms: 1.57x faster                                  |
| pickle_pure_python      | 452 us                                                 | 289 us: 1.57x faster                                   |
| hexiom                  | 9.43 ms                                                | 6.07 ms: 1.55x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.33 ms: 1.53x faster                                  |
| nbody                   | 144 ms                                                 | 93.9 ms: 1.53x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 76.4 ms: 1.53x faster                                  |
| chaos                   | 106 ms                                                 | 69.7 ms: 1.52x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.1 us: 1.52x faster                                  |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                  |
| mako                    | 14.7 ms                                                | 9.75 ms: 1.50x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.63 ms: 1.49x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 203 us: 1.49x faster                                   |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.48x faster                                   |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                  |
| html5lib                | 85.9 ms                                                | 59.1 ms: 1.45x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                 |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.49 ms: 1.42x faster                                  |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.41x faster                                 |
| pprint_safe_repr        | 953 ms                                                 | 678 ms: 1.41x faster                                   |
| xml_etree_process       | 74.5 ms                                                | 53.1 ms: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                   |
| chameleon               | 9.17 ms                                                | 6.60 ms: 1.39x faster                                  |
| logging_simple          | 8.10 us                                                | 5.84 us: 1.39x faster                                  |
| tornado_http            | 128 ms                                                 | 93.1 ms: 1.38x faster                                  |
| logging_format          | 8.85 us                                                | 6.47 us: 1.37x faster                                  |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                 |
| async_tree_none         | 711 ms                                                 | 530 ms: 1.34x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                  |
| scimark_fft             | 421 ms                                                 | 317 ms: 1.33x faster                                   |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                   |
| fannkuch                | 488 ms                                                 | 371 ms: 1.31x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.89 us: 1.31x faster                                  |
| coroutines              | 31.6 ms                                                | 24.4 ms: 1.30x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 732 ms: 1.30x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.22 ms: 1.29x faster                                  |
| genshi_xml              | 63.7 ms                                                | 49.7 ms: 1.28x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 670 ms: 1.28x faster                                   |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 51.6 ms: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 80.3 ms: 1.25x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 75.5 ms: 1.24x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.3 ms: 1.24x faster                                  |
| json_loads              | 28.7 us                                                | 23.5 us: 1.22x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 48.7 ns: 1.22x faster                                  |
| pickle_list             | 4.72 us                                                | 3.96 us: 1.19x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.18x faster                                   |
| pylint                  | 532 ms                                                 | 455 ms: 1.17x faster                                   |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                  |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                  |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| mdp                     | 2.74 sec                                               | 2.48 sec: 1.11x faster                                 |
| regex_v8                | 25.0 ms                                                | 22.7 ms: 1.10x faster                                  |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| generators              | 76.4 ms                                                | 70.6 ms: 1.08x faster                                  |
| unpickle                | 14.2 us                                                | 13.3 us: 1.07x faster                                  |
| telco                   | 6.73 ms                                                | 6.54 ms: 1.03x faster                                  |
| regex_dna               | 214 ms                                                 | 209 ms: 1.02x faster                                   |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                  |
| pickle                  | 10.2 us                                                | 10.3 us: 1.02x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.06 ms: 1.05x slower                                  |
| pidigits                | 190 ms                                                 | 199 ms: 1.05x slower                                   |
| pickle_dict             | 27.6 us                                                | 31.0 us: 1.12x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.66 ms: 1.15x slower                                  |
| coverage                | 74.7 ms                                                | 97.8 ms: 1.31x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221022-3.12.0a1+-f58631b/bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b.json: mypy
