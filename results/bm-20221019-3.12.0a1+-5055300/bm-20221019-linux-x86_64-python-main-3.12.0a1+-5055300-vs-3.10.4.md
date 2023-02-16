
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5055300
- commit date: 2022-10-19
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.46 ms: 1.42x faster                                  |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                  |
| tornado_http   | 128 ms                                                 | 93.0 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 109 ms                                                 | 71.1 ms: 1.53x faster                                  |
| nbody          | 144 ms                                                 | 94.8 ms: 1.52x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                  |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.40 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.59x faster                                   |
| unpickle_pure_python | 302 us                                                 | 202 us: 1.49x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.42 ms: 1.43x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 53.3 ms: 1.40x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.9 ms: 1.22x faster                                  |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                  |
| pickle_list          | 4.72 us                                                | 3.99 us: 1.18x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 144 ms: 1.13x faster                                   |
| unpickle             | 14.2 us                                                | 13.3 us: 1.07x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| unpickle_list        | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.1 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.32 ms: 1.69x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.03 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.79 ms: 1.50x faster                                  |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.46x faster                                  |
| django_template | 46.3 ms                                                | 32.7 ms: 1.41x faster                                  |
| genshi_xml      | 63.7 ms                                                | 49.3 ms: 1.29x faster                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.36 ms: 2.17x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                   |
| logging_silent          | 176 ns                                                 | 93.3 ns: 1.89x faster                                  |
| python_startup          | 14.1 ms                                                | 8.32 ms: 1.69x faster                                  |
| richards                | 75.2 ms                                                | 45.2 ms: 1.66x faster                                  |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                   |
| pyflate                 | 676 ms                                                 | 409 ms: 1.65x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 67.0 ms: 1.62x faster                                  |
| raytrace                | 467 ms                                                 | 289 ms: 1.61x faster                                   |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.59x faster                                   |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                  |
| chaos                   | 106 ms                                                 | 67.8 ms: 1.56x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 75.4 ms: 1.55x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.11 ms: 1.54x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.33 ms: 1.54x faster                                  |
| float                   | 109 ms                                                 | 71.1 ms: 1.53x faster                                  |
| nbody                   | 144 ms                                                 | 94.8 ms: 1.52x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.5 us: 1.50x faster                                  |
| mako                    | 14.7 ms                                                | 9.79 ms: 1.50x faster                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                   |
| unpickle_pure_python    | 302 us                                                 | 202 us: 1.49x faster                                   |
| sqlglot_transpile       | 2.43 ms                                                | 1.63 ms: 1.49x faster                                  |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.46x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.44x faster                                 |
| json_dumps              | 13.4 ms                                                | 9.42 ms: 1.43x faster                                  |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 669 ms: 1.43x faster                                   |
| chameleon               | 9.17 ms                                                | 6.46 ms: 1.42x faster                                  |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.41x faster                                  |
| pycparser               | 1.53 sec                                               | 1.08 sec: 1.41x faster                                 |
| xml_etree_process       | 74.5 ms                                                | 53.3 ms: 1.40x faster                                  |
| thrift                  | 1.03 ms                                                | 742 us: 1.39x faster                                   |
| logging_simple          | 8.10 us                                                | 5.83 us: 1.39x faster                                  |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                   |
| tornado_http            | 128 ms                                                 | 93.0 ms: 1.38x faster                                  |
| logging_format          | 8.85 us                                                | 6.49 us: 1.36x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                 |
| scimark_fft             | 421 ms                                                 | 311 ms: 1.35x faster                                   |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                   |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                  |
| fannkuch                | 488 ms                                                 | 363 ms: 1.35x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                  |
| deepcopy                | 438 us                                                 | 333 us: 1.31x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.89 us: 1.31x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 657 ms: 1.30x faster                                   |
| unpack_sequence         | 59.4 ns                                                | 45.7 ns: 1.30x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 732 ms: 1.30x faster                                   |
| genshi_xml              | 63.7 ms                                                | 49.3 ms: 1.29x faster                                  |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                  |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                  |
| dulwich_log             | 75.8 ms                                                | 61.2 ms: 1.24x faster                                  |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 76.9 ms: 1.22x faster                                  |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                  |
| pickle_list             | 4.72 us                                                | 3.99 us: 1.18x faster                                  |
| pylint                  | 532 ms                                                 | 454 ms: 1.17x faster                                   |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                  |
| sympy_str               | 325 ms                                                 | 280 ms: 1.16x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 144 ms: 1.13x faster                                   |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                   |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.13x faster                                  |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.12x faster                                   |
| json                    | 5.35 ms                                                | 4.77 ms: 1.12x faster                                  |
| generators              | 76.4 ms                                                | 71.4 ms: 1.07x faster                                  |
| unpickle                | 14.2 us                                                | 13.3 us: 1.07x faster                                  |
| telco                   | 6.73 ms                                                | 6.43 ms: 1.05x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                   |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                   |
| mdp                     | 2.74 sec                                               | 2.69 sec: 1.02x faster                                 |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                   |
| unpickle_list           | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.03 ms: 1.04x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.40 ms: 1.06x slower                                  |
| pickle_dict             | 27.6 us                                                | 31.1 us: 1.13x slower                                  |
| coverage                | 74.7 ms                                                | 97.7 ms: 1.31x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221019-3.12.0a1+-5055300/bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300.json: mypy
