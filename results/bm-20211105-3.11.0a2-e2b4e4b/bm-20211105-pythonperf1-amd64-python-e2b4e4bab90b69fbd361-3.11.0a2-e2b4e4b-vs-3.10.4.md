
# Results vs. 3.10.4

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: windows-amd64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 210 ms: 1.13x faster                                                       |
| chameleon      | 5.92 ms                                                     | 5.53 ms: 1.07x faster                                                      |
| docutils       | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                                     |
| html5lib       | 46.5 ms                                                     | 41.4 ms: 1.12x faster                                                      |
| tornado_http   | 109 ms                                                      | 98.3 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.1 ms: 1.07x faster                                                      |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                                       |
| nbody          | 69.3 ms                                                     | 90.3 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 90.4 ms: 1.14x faster                                                      |
| regex_dna      | 132 ms                                                      | 131 ms: 1.01x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.82 ms: 1.09x slower                                                      |
| regex_v8       | 15.0 ms                                                     | 16.6 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle             | 9.17 us                                                     | 7.81 us: 1.17x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 228 us: 1.13x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.54 us: 1.11x faster                                                      |
| xml_etree_process    | 43.4 ms                                                     | 39.7 ms: 1.09x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 93.8 ms: 1.09x faster                                                      |
| json_dumps           | 8.50 ms                                                     | 7.94 ms: 1.07x faster                                                      |
| pickle_dict          | 16.9 us                                                     | 16.2 us: 1.04x faster                                                      |
| pickle_list          | 2.59 us                                                     | 2.49 us: 1.04x faster                                                      |
| pickle               | 6.80 us                                                     | 6.61 us: 1.03x faster                                                      |
| unpickle_pure_python | 171 us                                                      | 168 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.2 ms: 1.03x slower                                                      |
| json_loads           | 14.2 us                                                     | 14.9 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.8 ms: 1.06x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 15.1 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 8.07 ms: 1.09x faster                                                      |
| genshi_text     | 19.0 ms                                                     | 17.5 ms: 1.09x faster                                                      |
| django_template | 28.2 ms                                                     | 26.0 ms: 1.08x faster                                                      |
| genshi_xml      | 40.5 ms                                                     | 38.5 ms: 1.05x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20211105-pythonperf1-amd64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.86 ms: 1.46x faster                                                      |
| async_tree_none         | 420 ms                                                      | 307 ms: 1.37x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 793 ms: 1.34x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 72.1 ns: 1.34x faster                                                      |
| go                      | 136 ms                                                      | 106 ms: 1.28x faster                                                       |
| raytrace                | 271 ms                                                      | 214 ms: 1.27x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 395 ms: 1.26x faster                                                       |
| richards                | 41.2 ms                                                     | 34.0 ms: 1.21x faster                                                      |
| unpickle                | 9.17 us                                                     | 7.81 us: 1.17x faster                                                      |
| async_generators        | 224 ms                                                      | 192 ms: 1.17x faster                                                       |
| thrift                  | 615 us                                                      | 528 us: 1.17x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 530 ms: 1.15x faster                                                       |
| regex_compile           | 103 ms                                                      | 90.4 ms: 1.14x faster                                                      |
| create_gc_cycles        | 782 us                                                      | 686 us: 1.14x faster                                                       |
| logging_simple          | 6.20 us                                                     | 5.45 us: 1.14x faster                                                      |
| docutils                | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                                     |
| pycparser               | 868 ms                                                      | 769 ms: 1.13x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 228 us: 1.13x faster                                                       |
| 2to3                    | 237 ms                                                      | 210 ms: 1.13x faster                                                       |
| logging_format          | 6.66 us                                                     | 5.92 us: 1.12x faster                                                      |
| html5lib                | 46.5 ms                                                     | 41.4 ms: 1.12x faster                                                      |
| tornado_http            | 109 ms                                                      | 98.3 ms: 1.11x faster                                                      |
| unpickle_list           | 2.81 us                                                     | 2.54 us: 1.11x faster                                                      |
| xml_etree_process       | 43.4 ms                                                     | 39.7 ms: 1.09x faster                                                      |
| chaos                   | 58.9 ms                                                     | 53.9 ms: 1.09x faster                                                      |
| hexiom                  | 5.52 ms                                                     | 5.06 ms: 1.09x faster                                                      |
| mako                    | 8.80 ms                                                     | 8.07 ms: 1.09x faster                                                      |
| genshi_text             | 19.0 ms                                                     | 17.5 ms: 1.09x faster                                                      |
| xml_etree_parse         | 102 ms                                                      | 93.8 ms: 1.09x faster                                                      |
| django_template         | 28.2 ms                                                     | 26.0 ms: 1.08x faster                                                      |
| scimark_monte_carlo     | 55.9 ms                                                     | 51.7 ms: 1.08x faster                                                      |
| pyflate                 | 387 ms                                                      | 358 ms: 1.08x faster                                                       |
| pylint                  | 347 ms                                                      | 321 ms: 1.08x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 44.1 ms: 1.08x faster                                                      |
| sqlalchemy_declarative  | 95.4 ms                                                     | 88.5 ms: 1.08x faster                                                      |
| pprint_safe_repr        | 589 ms                                                      | 547 ms: 1.08x faster                                                       |
| float                   | 60.2 ms                                                     | 56.1 ms: 1.07x faster                                                      |
| pprint_pformat          | 1.21 sec                                                    | 1.13 sec: 1.07x faster                                                     |
| json_dumps              | 8.50 ms                                                     | 7.94 ms: 1.07x faster                                                      |
| chameleon               | 5.92 ms                                                     | 5.53 ms: 1.07x faster                                                      |
| mdp                     | 1.71 sec                                                    | 1.61 sec: 1.06x faster                                                     |
| python_startup          | 20.0 ms                                                     | 18.8 ms: 1.06x faster                                                      |
| crypto_pyaes            | 62.3 ms                                                     | 58.9 ms: 1.06x faster                                                      |
| pathlib                 | 77.4 ms                                                     | 73.4 ms: 1.05x faster                                                      |
| genshi_xml              | 40.5 ms                                                     | 38.5 ms: 1.05x faster                                                      |
| scimark_lu              | 85.4 ms                                                     | 81.5 ms: 1.05x faster                                                      |
| bench_thread_pool       | 946 us                                                      | 906 us: 1.04x faster                                                       |
| pickle_dict             | 16.9 us                                                     | 16.2 us: 1.04x faster                                                      |
| pickle_list             | 2.59 us                                                     | 2.49 us: 1.04x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 37.5 ms: 1.04x faster                                                      |
| dask                    | 305 ms                                                      | 295 ms: 1.03x faster                                                       |
| scimark_sor             | 105 ms                                                      | 101 ms: 1.03x faster                                                       |
| sqlalchemy_imperative   | 11.0 ms                                                     | 10.6 ms: 1.03x faster                                                      |
| sympy_integrate         | 14.8 ms                                                     | 14.4 ms: 1.03x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 196 ms: 1.03x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.1 ms: 1.03x faster                                                      |
| pickle                  | 6.80 us                                                     | 6.61 us: 1.03x faster                                                      |
| sqlite_synth            | 1.84 us                                                     | 1.80 us: 1.02x faster                                                      |
| sympy_sum               | 104 ms                                                      | 102 ms: 1.02x faster                                                       |
| generators              | 31.6 ms                                                     | 31.0 ms: 1.02x faster                                                      |
| unpickle_pure_python    | 171 us                                                      | 168 us: 1.02x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 28.1 us: 1.01x faster                                                      |
| sympy_expand            | 315 ms                                                      | 311 ms: 1.01x faster                                                       |
| regex_dna               | 132 ms                                                      | 131 ms: 1.01x faster                                                       |
| json                    | 3.05 ms                                                     | 3.06 ms: 1.01x slower                                                      |
| bench_mp_pool           | 60.7 ms                                                     | 61.4 ms: 1.01x slower                                                      |
| sympy_str               | 188 ms                                                      | 191 ms: 1.01x slower                                                       |
| pidigits                | 145 ms                                                      | 148 ms: 1.02x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.37 ms: 1.02x slower                                                      |
| sqlglot_transpile       | 1.46 ms                                                     | 1.50 ms: 1.02x slower                                                      |
| xml_etree_iterparse     | 63.5 ms                                                     | 65.2 ms: 1.03x slower                                                      |
| telco                   | 3.78 ms                                                     | 3.91 ms: 1.03x slower                                                      |
| deepcopy_reduce         | 2.16 us                                                     | 2.23 us: 1.04x slower                                                      |
| deepcopy                | 255 us                                                      | 266 us: 1.04x slower                                                       |
| meteor_contest          | 72.5 ms                                                     | 76.2 ms: 1.05x slower                                                      |
| json_loads              | 14.2 us                                                     | 14.9 us: 1.05x slower                                                      |
| spectral_norm           | 78.0 ms                                                     | 82.7 ms: 1.06x slower                                                      |
| sqlglot_parse           | 1.22 ms                                                     | 1.29 ms: 1.06x slower                                                      |
| fannkuch                | 258 ms                                                      | 275 ms: 1.07x slower                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.82 ms: 1.09x slower                                                      |
| scimark_fft             | 193 ms                                                      | 212 ms: 1.10x slower                                                       |
| regex_v8                | 15.0 ms                                                     | 16.6 ms: 1.11x slower                                                      |
| coroutines              | 15.9 ms                                                     | 18.1 ms: 1.14x slower                                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 3.18 ms: 1.19x slower                                                      |
| comprehensions          | 16.0 us                                                     | 19.1 us: 1.19x slower                                                      |
| nbody                   | 69.3 ms                                                     | 90.3 ms: 1.30x slower                                                      |
| unpack_sequence         | 37.8 ns                                                     | 51.9 ns: 1.37x slower                                                      |
| coverage                | 40.0 ms                                                     | 262 ms: 6.54x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (4): asyncio_tcp, flaskblogging, nqueens, xml_etree_generate
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, mypy2, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
