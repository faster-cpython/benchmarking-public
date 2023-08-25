
# Results vs. 3.10.4

- fork: python
- ref: 5a7e1e0a92622c605ab2
- machine: windows-amd64
- commit hash: 5a7e1e0
- commit date: 2022-07-11
- overall geometric mean: 1.11x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 206 ms: 1.15x faster                                                       |
| chameleon      | 5.92 ms                                                     | 5.14 ms: 1.15x faster                                                      |
| docutils       | 1.89 sec                                                    | 1.58 sec: 1.20x faster                                                     |
| html5lib       | 46.5 ms                                                     | 38.9 ms: 1.19x faster                                                      |
| tornado_http   | 109 ms                                                      | 91.9 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.9 ms: 1.12x faster                                                      |
| nbody          | 69.3 ms                                                     | 68.7 ms: 1.01x faster                                                      |
| pidigits       | 145 ms                                                      | 146 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 132 ms                                                      | 114 ms: 1.15x faster                                                       |
| regex_compile  | 103 ms                                                      | 90.8 ms: 1.14x faster                                                      |
| regex_v8       | 15.0 ms                                                     | 13.4 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.70 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 257 us                                                      | 204 us: 1.26x faster                                                       |
| xml_etree_process    | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                                      |
| unpickle_pure_python | 171 us                                                      | 152 us: 1.13x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.32 us: 1.10x faster                                                      |
| json_dumps           | 8.50 ms                                                     | 7.78 ms: 1.09x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 95.1 ms: 1.07x faster                                                      |
| pickle               | 6.80 us                                                     | 6.48 us: 1.05x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 53.4 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 62.7 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                     | 14.1 us: 1.01x faster                                                      |
| pickle_list          | 2.59 us                                                     | 2.65 us: 1.03x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.4 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.4 ms: 1.09x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 15.4 ms: 1.01x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.23 ms: 1.22x faster                                                      |
| django_template | 28.2 ms                                                     | 25.0 ms: 1.13x faster                                                      |
| genshi_text     | 19.0 ms                                                     | 17.6 ms: 1.08x faster                                                      |
| genshi_xml      | 40.5 ms                                                     | 38.6 ms: 1.05x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220711-pythonperf1-amd64-python-5a7e1e0a92622c605ab2-3.11.0b4-5a7e1e0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.66 ms: 1.57x faster                                                      |
| async_tree_io           | 1.07 sec                                                    | 753 ms: 1.42x faster                                                       |
| go                      | 136 ms                                                      | 99.5 ms: 1.37x faster                                                      |
| scimark_lu              | 85.4 ms                                                     | 62.7 ms: 1.36x faster                                                      |
| scimark_sor             | 105 ms                                                      | 78.5 ms: 1.34x faster                                                      |
| logging_silent          | 96.4 ns                                                     | 72.4 ns: 1.33x faster                                                      |
| raytrace                | 271 ms                                                      | 204 ms: 1.33x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 375 ms: 1.33x faster                                                       |
| async_tree_none         | 420 ms                                                      | 317 ms: 1.33x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 936 us: 1.30x faster                                                       |
| richards                | 41.2 ms                                                     | 31.7 ms: 1.30x faster                                                      |
| sqlglot_transpile       | 1.46 ms                                                     | 1.13 ms: 1.29x faster                                                      |
| mypy2                   | 352 ms                                                      | 278 ms: 1.27x faster                                                       |
| pyflate                 | 387 ms                                                      | 306 ms: 1.27x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 44.3 ms: 1.26x faster                                                      |
| async_generators        | 224 ms                                                      | 178 ms: 1.26x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 204 us: 1.26x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 50.6 ms: 1.23x faster                                                      |
| pycparser               | 868 ms                                                      | 706 ms: 1.23x faster                                                       |
| mako                    | 8.80 ms                                                     | 7.23 ms: 1.22x faster                                                      |
| chaos                   | 58.9 ms                                                     | 48.7 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed | 609 ms                                                      | 508 ms: 1.20x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.58 sec: 1.20x faster                                                     |
| hexiom                  | 5.52 ms                                                     | 4.61 ms: 1.20x faster                                                      |
| html5lib                | 46.5 ms                                                     | 38.9 ms: 1.19x faster                                                      |
| thrift                  | 615 us                                                      | 518 us: 1.19x faster                                                       |
| tornado_http            | 109 ms                                                      | 91.9 ms: 1.19x faster                                                      |
| create_gc_cycles        | 782 us                                                      | 664 us: 1.18x faster                                                       |
| aiohttp                 | 1.01 ms                                                     | 860 us: 1.17x faster                                                       |
| chameleon               | 5.92 ms                                                     | 5.14 ms: 1.15x faster                                                      |
| regex_dna               | 132 ms                                                      | 114 ms: 1.15x faster                                                       |
| 2to3                    | 237 ms                                                      | 206 ms: 1.15x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                                      |
| pprint_safe_repr        | 589 ms                                                      | 515 ms: 1.14x faster                                                       |
| regex_compile           | 103 ms                                                      | 90.8 ms: 1.14x faster                                                      |
| pprint_pformat          | 1.21 sec                                                    | 1.07 sec: 1.13x faster                                                     |
| dask                    | 305 ms                                                      | 270 ms: 1.13x faster                                                       |
| django_template         | 28.2 ms                                                     | 25.0 ms: 1.13x faster                                                      |
| unpickle_pure_python    | 171 us                                                      | 152 us: 1.13x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 25.3 us: 1.13x faster                                                      |
| sqlalchemy_declarative  | 95.4 ms                                                     | 84.7 ms: 1.13x faster                                                      |
| regex_v8                | 15.0 ms                                                     | 13.4 ms: 1.12x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 34.8 ms: 1.12x faster                                                      |
| float                   | 60.2 ms                                                     | 53.9 ms: 1.12x faster                                                      |
| bench_thread_pool       | 946 us                                                      | 858 us: 1.10x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.32 us: 1.10x faster                                                      |
| json_dumps              | 8.50 ms                                                     | 7.78 ms: 1.09x faster                                                      |
| pylint                  | 347 ms                                                      | 318 ms: 1.09x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.4 ms: 1.09x faster                                                      |
| sympy_sum               | 104 ms                                                      | 95.8 ms: 1.09x faster                                                      |
| sqlite_synth            | 1.84 us                                                     | 1.70 us: 1.09x faster                                                      |
| genshi_text             | 19.0 ms                                                     | 17.6 ms: 1.08x faster                                                      |
| sympy_integrate         | 14.8 ms                                                     | 13.7 ms: 1.08x faster                                                      |
| sympy_expand            | 315 ms                                                      | 291 ms: 1.08x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 44.2 ms: 1.08x faster                                                      |
| coroutines              | 15.9 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| xml_etree_parse         | 102 ms                                                      | 95.1 ms: 1.07x faster                                                      |
| pathlib                 | 77.4 ms                                                     | 72.4 ms: 1.07x faster                                                      |
| spectral_norm           | 78.0 ms                                                     | 73.7 ms: 1.06x faster                                                      |
| asyncio_tcp             | 712 ms                                                      | 675 ms: 1.06x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 192 ms: 1.05x faster                                                       |
| sqlalchemy_imperative   | 11.0 ms                                                     | 10.4 ms: 1.05x faster                                                      |
| genshi_xml              | 40.5 ms                                                     | 38.6 ms: 1.05x faster                                                      |
| pickle                  | 6.80 us                                                     | 6.48 us: 1.05x faster                                                      |
| deepcopy                | 255 us                                                      | 246 us: 1.04x faster                                                       |
| scimark_fft             | 193 ms                                                      | 186 ms: 1.04x faster                                                       |
| sympy_str               | 188 ms                                                      | 182 ms: 1.03x faster                                                       |
| fannkuch                | 258 ms                                                      | 251 ms: 1.03x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.67 sec: 1.03x faster                                                     |
| xml_etree_generate      | 54.5 ms                                                     | 53.4 ms: 1.02x faster                                                      |
| comprehensions          | 16.0 us                                                     | 15.7 us: 1.01x faster                                                      |
| xml_etree_iterparse     | 63.5 ms                                                     | 62.7 ms: 1.01x faster                                                      |
| python_startup_no_site  | 15.5 ms                                                     | 15.4 ms: 1.01x faster                                                      |
| nbody                   | 69.3 ms                                                     | 68.7 ms: 1.01x faster                                                      |
| json_loads              | 14.2 us                                                     | 14.1 us: 1.01x faster                                                      |
| pidigits                | 145 ms                                                      | 146 ms: 1.01x slower                                                       |
| nqueens                 | 67.0 ms                                                     | 67.6 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.68 ms: 1.01x slower                                                      |
| bench_mp_pool           | 60.7 ms                                                     | 61.4 ms: 1.01x slower                                                      |
| regex_effbot            | 1.66 ms                                                     | 1.70 ms: 1.02x slower                                                      |
| pickle_list             | 2.59 us                                                     | 2.65 us: 1.03x slower                                                      |
| meteor_contest          | 72.5 ms                                                     | 74.8 ms: 1.03x slower                                                      |
| gc_traversal            | 1.34 ms                                                     | 1.41 ms: 1.05x slower                                                      |
| telco                   | 3.78 ms                                                     | 4.02 ms: 1.06x slower                                                      |
| generators              | 31.6 ms                                                     | 33.9 ms: 1.07x slower                                                      |
| logging_simple          | 6.20 us                                                     | 6.68 us: 1.08x slower                                                      |
| logging_format          | 6.66 us                                                     | 7.19 us: 1.08x slower                                                      |
| pickle_dict             | 16.9 us                                                     | 18.4 us: 1.09x slower                                                      |
| json                    | 3.05 ms                                                     | 3.32 ms: 1.09x slower                                                      |
| unpack_sequence         | 37.8 ns                                                     | 45.4 ns: 1.20x slower                                                      |
| coverage                | 40.0 ms                                                     | 54.1 ms: 1.35x slower                                                      |
| Geometric mean          | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (3): unpickle_list, deepcopy_reduce, flaskblogging
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x
