
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 57be545
- commit date: 2022-11-12
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 246 ms: 1.37x faster                                   |
| chameleon      | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| html5lib       | 85.9 ms                                                | 58.9 ms: 1.46x faster                                  |
| tornado_http   | 127 ms                                                 | 92.5 ms: 1.38x faster                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.4 ms: 1.52x faster                                  |
| float          | 111 ms                                                 | 73.3 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                   |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.0 ms: 1.41x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.8 ms: 1.23x faster                                  |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| pickle_list          | 4.56 us                                                | 4.14 us: 1.10x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                  |
| pickle               | 10.3 us                                                | 10.0 us: 1.02x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.52 ms: 1.66x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.24 ms: 1.07x slower                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.70 ms: 1.52x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.3 ms: 1.42x faster                                  |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                  |
| genshi_xml      | 63.3 ms                                                | 46.8 ms: 1.35x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                  |
| logging_silent          | 175 ns                                                 | 91.8 ns: 1.91x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.90x faster                                   |
| richards                | 74.9 ms                                                | 41.7 ms: 1.80x faster                                  |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                   |
| pyflate                 | 673 ms                                                 | 402 ms: 1.68x faster                                   |
| python_startup          | 14.2 ms                                                | 8.52 ms: 1.66x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 65.5 ms: 1.65x faster                                  |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                   |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                   |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.59x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 75.1 ms: 1.58x faster                                  |
| spectral_norm           | 150 ms                                                 | 95.2 ms: 1.58x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.13 ms: 1.55x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.35 ms: 1.53x faster                                  |
| mako                    | 14.8 ms                                                | 9.70 ms: 1.52x faster                                  |
| nbody                   | 142 ms                                                 | 93.4 ms: 1.52x faster                                  |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.52x faster                                   |
| float                   | 111 ms                                                 | 73.3 ms: 1.51x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.64 ms: 1.50x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 44.2 ns: 1.46x faster                                  |
| html5lib                | 85.9 ms                                                | 58.9 ms: 1.46x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.3 ms: 1.42x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.0 ms: 1.41x faster                                  |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.34 us: 1.40x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.40x faster                                 |
| logging_simple          | 8.07 us                                                | 5.77 us: 1.40x faster                                  |
| chameleon               | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 688 ms: 1.39x faster                                   |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                   |
| aiohttp                 | 1.38 ms                                                | 998 us: 1.39x faster                                   |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                   |
| tornado_http            | 127 ms                                                 | 92.5 ms: 1.38x faster                                  |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                   |
| 2to3                    | 336 ms                                                 | 246 ms: 1.37x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                  |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                   |
| genshi_xml              | 63.3 ms                                                | 46.8 ms: 1.35x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                 |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                 |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                  |
| coroutines              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.16 ms: 1.31x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 731 ms: 1.30x faster                                   |
| fannkuch                | 486 ms                                                 | 374 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.5 ms: 1.30x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                   |
| dulwich_log             | 75.9 ms                                                | 61.1 ms: 1.24x faster                                  |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.8 ms: 1.23x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.19x faster                                  |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| sympy_expand            | 545 ms                                                 | 458 ms: 1.19x faster                                   |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                   |
| json                    | 5.42 ms                                                | 4.71 ms: 1.15x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                  |
| mdp                     | 2.82 sec                                               | 2.47 sec: 1.14x faster                                 |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.65 us: 1.11x faster                                  |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                   |
| pickle_list             | 4.56 us                                                | 4.14 us: 1.10x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                   |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                   |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                  |
| telco                   | 6.54 ms                                                | 6.32 ms: 1.04x faster                                  |
| pickle                  | 10.3 us                                                | 10.0 us: 1.02x faster                                  |
| unpickle_list           | 4.82 us                                                | 4.91 us: 1.02x slower                                  |
| generators              | 76.8 ms                                                | 79.6 ms: 1.04x slower                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.24 ms: 1.07x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.64 ms: 1.13x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| coverage                | 72.8 ms                                                | 99.8 ms: 1.37x slower                                  |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221112-3.12.0a2+-57be545/bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x
